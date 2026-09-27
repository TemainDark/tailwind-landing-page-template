"""Bangkok flood outlook: ensemble-driven bucket model per district.

Inputs in ./data (created by fetch_inputs.py):
  geo.json                    district geometry + centroids (OSM)
  elev_samples.json           DEM samples per district (Copernicus via Open-Meteo)
  om_district_bestmatch.json  Open-Meteo best-match daily rain per district (past 21 d + 16 d)
  ens_zones.json              Open-Meteo ensemble daily rain for 6 zones (ECMWF IFS/AIFS, GEFS, GEPS...)
  era5_bkk.json               ERA5 daily rain 1991-2025 (climatological analogues)
  tide_pred.json              harmonic tide prediction at the Chao Phraya mouth (m MSL)
  glofas.json                 GloFAS river discharge (Chao Phraya at Bangkok)
plus obs.py (observed situation from news, rain calibration, river observations).
Output: data/model_out.json
"""
import json, math, os, random, sys
import numpy as np
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(os.path.join(HERE, 'data'))

from districts_static import D
from obs import OBS_DATE, OBS_LEVEL, OBS_HIST, OBS_RAIN_FACTOR, RIVER, NORMAL_OCT_MM, ANALOG_FACTOR, TIDE_SEASONAL, NOTES

rng = np.random.default_rng(20260926)
random.seed(20260926)

geo = json.load(open('geo.json'))
names = [d['en'] for d in geo['districts']]
pos = {d['en']: (d['lon'], d['lat']) for d in geo['districts']}
area = {d['en']: d['area'] for d in geo['districts']}

START, TODAY, END = date(2026, 9, 20), date.fromisoformat(OBS_DATE), date(2026, 10, 25)
days = [START + timedelta(i) for i in range((END - START).days + 1)]
ds = [d.isoformat() for d in days]
T0 = ds.index(TODAY.isoformat())
NF = len(ds) - T0  # forecast days incl. today

# ---------------- DEM blend for lowness ----------------
el = json.load(open('elev_samples.json'))
from collections import defaultdict
ev = defaultdict(list)
for (n, x, y), e in zip(el['pts'], el['elev']):
    if e is not None:
        ev[n].append(e)
low = {}
for n in names:
    p25 = float(np.percentile(ev[n], 25)) if ev[n] else 4.0
    dem_low = min(1, max(0, (5.5 - p25) / 4.5))
    low[n] = 0.7 * D[n]['low'] + 0.3 * dem_low

# ---------------- past rain (per district) ----------------
bm = json.load(open('om_district_bestmatch.json'))
past = {}
for n in names:
    t = bm[n]['daily']['time']; p = bm[n]['daily']['precipitation_sum']
    past[n] = {a: (b or 0.0) for a, b in zip(t, p)}
past_days = [t for t in bm[names[0]]['daily']['time'] if t < TODAY.isoformat()]
for n in names:  # calibrate the extreme event to observations
    for dd, f in OBS_RAIN_FACTOR(n).items():
        if dd in past[n]:
            past[n][dd] *= f

# ---------------- tide & river ----------------
tp = json.load(open('tide_pred.json'))
tmax = {}; ttime = {}
for t, h in zip(tp['hourly_t'], tp['hourly_h']):
    d0 = t[:10]
    extra = TIDE_SEASONAL * max(0, (date.fromisoformat(d0) - date(2026, 10, 1)).days)
    h = h + extra
    if d0 not in tmax or h > tmax[d0]:
        tmax[d0] = h; ttime[d0] = t[11:16]
gl = json.load(open('glofas.json'))[0]['daily']
gq = dict(zip(gl['time'], gl['river_discharge']))
gq_med = dict(zip(gl['time'], gl['river_discharge_median']))
gq_max = dict(zip(gl['time'], gl['river_discharge_max']))

def river_q(d0, key=gq):
    """Real-world discharge estimate at Bangkok: GloFAS relative change applied to observed flow."""
    ref = gq[RIVER['ref_date']]
    v = key.get(d0)
    if v is None:
        v = key[max(k for k in key if k <= d0)]
    q = RIVER['q_obs'] * (1 + (v / ref - 1) * RIVER['damp'])
    return min(RIVER['qmax'], max(RIVER['qmin'], q))

def river_level(d0, q):
    """Approx. water level at Pak Khlong Talat / Memorial Bridge, m MSL."""
    return tmax[d0] + RIVER['a'] + RIVER['b'] * (q - RIVER['q0'])

# ---------------- ensembles -> traces ----------------
ens = json.load(open('ens_zones.json'))
zones = ['C', 'N', 'E', 'SE', 'W', 'S']
zpos = {'C': (100.535, 13.745), 'N': (100.60, 13.88), 'E': (100.80, 13.80),
        'SE': (100.64, 13.69), 'W': (100.40, 13.73), 'S': (100.45, 13.60)}
wz = {}
for n in names:
    x, y = pos[n]
    w = np.array([1 / (((x - zpos[z][0]) * 0.97) ** 2 + (y - zpos[z][1]) ** 2 + 0.0004) for z in zones])
    wz[n] = w / w.sum()
zone_of = {n: zones[int(np.argmax(wz[n]))] for n in names}

def member_matrix(model):
    """array [members, zones, NF] with NaN beyond horizon, aligned to TODAY."""
    z0 = ens[model]['C']
    t = z0['time']; i0 = t.index(TODAY.isoformat())
    M = len(z0['members'])
    out = np.full((M, len(zones), NF), np.nan)
    for zi, z in enumerate(zones):
        for m, ser in enumerate(ens[model][z]['members']):
            vals = ser[i0:i0 + NF]
            for k, v in enumerate(vals):
                if v is not None:
                    out[m, zi, k] = v
    return out

mats = {m: member_matrix(m) for m in ['ecmwf_ifs025', 'ecmwf_aifs025', 'gfs05', 'gem_global']}
ext_pool = np.concatenate([mats['gfs05'], mats['gem_global']], axis=0)

# ERA5 analogues, rescaled to the station normal
era = json.load(open('era5_bkk.json'))['daily']
era_d = dict(zip(era['time'], era['precipitation_sum']))
oct_era = np.mean([sum((era_d.get(f'{y}-10-{d:02d}') or 0) for d in range(1, 32)) for y in range(1991, 2026)])
clim_scale = NORMAL_OCT_MM / oct_era

def analog(year, k):
    d0 = TODAY + timedelta(k)
    v = era_d.get(f'{year}-{d0.month:02d}-{d0.day:02d}')
    return (v or 0.0) * clim_scale * ANALOG_FACTOR

def climatology_daily():
    out = []
    for k in range(-T0, NF):
        d0 = TODAY + timedelta(k)
        vals = [(era_d.get(f'{y}-{d0.month:02d}-{d0.day:02d}') or 0) * clim_scale for y in range(1991, 2026)]
        out.append(float(np.mean(vals)))
    # smooth with 7-day window
    a = np.array(out); sm = np.convolve(np.pad(a, 3, mode='edge'), np.ones(7) / 7, mode='valid')
    return sm

traces = []  # list of (weight, array [zones, NF])
def build(model, weight):
    M = mats[model]
    for m in range(M.shape[0]):
        tr = M[m].copy()
        year = int(rng.integers(1991, 2026))
        ext = ext_pool[int(rng.integers(0, ext_pool.shape[0]))]
        for k in range(NF):
            w_clim = min(0.85, max(0.0, (k - 9) / 14))  # fade to climatology after ~day 10
            if np.isnan(tr[0, k]) or rng.random() < w_clim:
                if rng.random() < max(w_clim, 0.5 if np.isnan(tr[0, k]) else 0):
                    tr[:, k] = analog(year, k) * np.exp(rng.normal(0, 0.35, len(zones)))
                else:
                    v = ext[:, k]
                    tr[:, k] = v if not np.isnan(v[0]) else analog(year, k)
        traces.append((weight / M.shape[0], tr))

build('ecmwf_ifs025', 0.36)
build('ecmwf_aifs025', 0.24)
build('gfs05', 0.22)
build('gem_global', 0.18)
W = np.array([w for w, _ in traces]); W = W / W.sum()
NT = len(traces)

# ---------------- bucket model ----------------
LV = [10, 30, 80, 190]  # thresholds of the displayed water index (mm) for levels 1..4
def level(x):
    return int(sum(x >= t for t in LV))

S_INIT = {0: 4, 1: 18, 2: 55, 3: 120, 4: 260}

def step(n, S, API, R, regAPI, cityAPI, d0):
    p = D[n]
    rc = p['rc'] * (0.55 + 0.45 * min(1.0, API / 120))
    inflow = rc * R
    ext = p['ext'] * max(0.0, regAPI - 90) * 0.06
    tf = 1 - p['tide'] * 0.5 * min(1, max(0, (tmax[d0] - 1.55) / 0.5))
    cong = 1 / (1 + max(0.0, cityAPI - 100) / 260)
    cap = p['D0'] * tf * cong
    peak = S + inflow + ext
    drained = min(peak, cap)
    disp = (S + inflow + ext - 0.5 * drained) * (0.8 + 0.4 * low[n])
    return peak - drained, disp

# history (deterministic, observed rain) from 5 Sep to yesterday
hist_disp = {n: {} for n in names}
S = {n: 0.0 for n in names}; API = {n: 0.0 for n in names}
for d0 in past_days:
    Rn = {n: past[n][d0] for n in names}
    for n in names:
        API[n] = API[n] * 0.85 + Rn[n]
    cityAPI = float(np.mean(list(API.values())))
    regAPI = float(np.mean([API[n] for n in names if D[n]['zone'] in ('east', 'outer')]))
    for n in names:
        S[n], disp = step(n, S[n], API[n], Rn[n], regAPI, cityAPI, d0 if d0 in tmax else min(tmax))
        hist_disp[n][d0] = disp
API_hist = dict(API)

# observed state this morning (news) -> initial storage
S_obs = {n: S_INIT[OBS_LEVEL[n]] for n in names}
# yesterday (25 Sep evening) shown as observed
for n in names:
    for d0, lv in OBS_HIST.items():  # past days shown as reported
        if d0 in hist_disp[n]:
            hist_disp[n][d0] = S_INIT[lv.get(n, 1)] * 0.95
    hist_disp[n]['2026-09-24'] = min(hist_disp[n]['2026-09-24'], 25.0)

# forecast per trace
disp_f = np.zeros((NT, len(names), NF))
rain_f = np.zeros((NT, len(names), NF))
for ti, (_, tr) in enumerate(traces):
    Sx = dict(S_obs); APx = dict(API_hist)
    zn = rng.normal(0, 1, (len(zones), NF)); dn = rng.normal(0, 1, (len(names), NF))
    for k in range(NF):
        d0 = ds[T0 + k]
        for i, n in enumerate(names):
            base = float(np.dot(wz[n], np.nan_to_num(tr[:, k])))
            noise = math.exp(0.30 * zn[zones.index(zone_of[n]), k] + 0.45 * dn[i, k] - (0.30 ** 2 + 0.45 ** 2) / 2)
            rain_f[ti, i, k] = base * noise
        for i, n in enumerate(names):
            APx[n] = APx[n] * 0.85 + rain_f[ti, i, k]
        cityAPI = float(np.mean(list(APx.values())))
        regAPI = float(np.mean([APx[n] for n in names if D[n]['zone'] in ('east', 'outer')]))
        for i, n in enumerate(names):
            Sx[n], disp = step(n, Sx[n], APx[n], rain_f[ti, i, k], regAPI, cityAPI, d0)
            disp_f[ti, i, k] = disp
    # today = observed morning state + today's rain: never below the observed level
    for i, n in enumerate(names):
        disp_f[ti, i, 0] = max(disp_f[ti, i, 0], S_INIT[OBS_LEVEL[n]] * 0.9)

def wquant(x, q):
    """weighted quantile along axis 0"""
    idx = np.argsort(x, axis=0)
    xs = np.take_along_axis(x, idx, axis=0)
    ws = W[idx]
    cw = np.cumsum(ws, axis=0)
    pos_ = (cw >= q).argmax(axis=0)
    return np.take_along_axis(xs, pos_[None], axis=0)[0]

out_d = {}
for i, n in enumerate(names):
    hist = [hist_disp[n].get(d0, 0) for d0 in ds[:T0]]
    q = {}
    for qn, qq in (('p10', 0.1), ('p50', 0.5), ('p90', 0.9)):
        fut = [float(wquant(disp_f[:, i, k:k + 1], qq)[0]) for k in range(NF)]
        q[qn] = ''.join(str(level(v)) for v in hist + fut)
    pr2 = [100 if level(v) >= 2 else 0 for v in hist] + [int(round(100 * float(np.sum(W * (disp_f[:, i, k] >= LV[1]))))) for k in range(NF)]
    pr3 = [100 if level(v) >= 3 else 0 for v in hist] + [int(round(100 * float(np.sum(W * (disp_f[:, i, k] >= LV[2]))))) for k in range(NF)]
    rain_med = [round(past[n].get(d0, 0), 1) for d0 in ds[:T0]] + [round(float(wquant(rain_f[:, i, k:k + 1], 0.5)[0]), 1) for k in range(NF)]
    out_d[n] = dict(p10=q['p10'], p50=q['p50'], p90=q['p90'], pr2=pr2, pr3=pr3, rain=rain_med, low=round(low[n], 2))

# city-level series
city_rain_tr = np.einsum('tik,i->tk', rain_f, np.array([area[n] for n in names]) / sum(area.values()))
city_obs = [round(float(np.average([past[n].get(d0, 0) for n in names], weights=[area[n] for n in names])), 1) for d0 in ds[:T0]]
cr = {qn: [round(float(wquant(city_rain_tr[:, k:k + 1], qq)[0]), 1) for k in range(NF)] for qn, qq in (('p10', 0.1), ('p25', 0.25), ('p50', 0.5), ('p75', 0.75), ('p90', 0.9))}
cr_mean = [round(float(np.sum(W * city_rain_tr[:, k])), 1) for k in range(NF)]
clim = [round(float(v), 1) for v in climatology_daily()]
cum_tr = np.cumsum(city_rain_tr, axis=1)
river = []
for d0 in ds:
    q_ = river_q(d0); qmx = river_q(d0, gq_max)
    river.append(dict(q=round(q_), qmax=round(qmx), lvl=round(river_level(d0, q_), 2), lvlmax=round(river_level(d0, qmx), 2)))

out = dict(
    days=ds, today=T0, lv=LV,
    districts=out_d,
    city=dict(obs=city_obs, fc=cr, mean=cr_mean, clim=clim,
              cum_p10=[round(float(wquant(cum_tr[:, k:k + 1], 0.1)[0])) for k in range(NF)],
              cum_p50=[round(float(wquant(cum_tr[:, k:k + 1], 0.5)[0])) for k in range(NF)],
              cum_p90=[round(float(wquant(cum_tr[:, k:k + 1], 0.9)[0])) for k in range(NF)]),
    tide=[dict(max=round(tmax[d0], 2), t=ttime[d0]) for d0 in ds],
    river=river,
    ntraces=NT,
    notes=NOTES,
)
json.dump(out, open('model_out.json', 'w'), ensure_ascii=False, separators=(',', ':'))

# ---- console summary ----
print('traces', NT, 'clim_scale', round(clim_scale, 2))
print('day        ' + ' '.join(d[5:] for d in ds))
for n in names:
    print(f"{n[:18]:18s} {out_d[n]['p50']}  p90 {out_d[n]['p90']}")
print('city rain p50', cr['p50'])
print('city rain mean', cr_mean)
print('clim', clim)
print('tide', [tmax[d0] for d0 in ds])
print('river', [(r['q'], r['lvl']) for r in river])
