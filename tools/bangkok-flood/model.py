"""Bangkok flood outlook: ensemble-driven bucket model per district.

Inputs in ./data (created by fetch_inputs.py):
  geo.json                    district geometry + centroids (OSM)
  elev_samples.json           DEM samples per district (Copernicus via Open-Meteo)
  om_district_bestmatch.json  Open-Meteo best-match daily rain per district (past 21 d + 16 d)
  ens_zones.json              Open-Meteo ensemble daily rain for 6 zones (ECMWF IFS/AIFS, GEFS, GEPS...)
  era5_bkk.json               ERA5 daily rain 1991-2025 (climatological analogues)
  tide_pred.json              harmonic tide prediction at the Chao Phraya mouth (m MSL)
  glofas.json                 GloFAS river discharge (Chao Phraya at Bangkok)
  obs_live.json               ThaiWater gauges, TMD, METAR (created by fetch_obs.py)
plus obs.py (observed situation from news, rain calibration, river observations) and carry.json
(the state handed over by the previous run, so a new day starts where the last run of yesterday ended).
Output: data/model_out.json, carry.json
"""
import json, math, os, random, sys
import numpy as np
from datetime import date, datetime, timedelta

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

live = json.load(open('obs_live.json')) if os.path.exists('obs_live.json') else {}
FETCHED = datetime.strptime(live['fetched'], '%Y-%m-%d %H:%M') if live.get('fetched') else None  # Bangkok time
# "today" = Bangkok date of the latest observations; obs.OBS_DATE is the morning the news levels describe
START, END = date(2026, 9, 20), date(2026, 10, 25)
TODAY = max(date.fromisoformat(OBS_DATE), FETCHED.date() if FETCHED else date.fromisoformat(OBS_DATE))
CARRY = os.path.join(HERE, 'carry.json')  # handed over by the previous run
carry = json.load(open(CARRY)) if os.path.exists(CARRY) else {}
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

def apply_gauge_totals():
    """replace model rain of past days by ThaiWater gauge totals (07:00 -> 07:00, IDW per district),
    including the totals of earlier days kept in carry.json; returns them for the next run"""
    got = {d0: v for d0, v in carry.get('rain', {}).items() if START.isoformat() <= d0 < TODAY.isoformat()}
    # quality of each day's totals: (2 = whole 07:00 -> 07:00 day, 1 = part of it; number of gauges)
    qual = {d0: tuple(carry.get('rain_q', {}).get(d0, (2, 100))) for d0 in got}
    n_y = sum(1 for g in gauges if g.get('yday') is not None)
    n_t = sum(1 for g in gauges if g.get('today') is not None)
    for dd, vals, q in ((obs_yday_date, obs_yday, (2, n_y)), (rain_day and rain_day.isoformat(), obs_today, (1, n_t))):
        if not dd or dd >= TODAY.isoformat() or q[1] < 30:  # right after midnight "yesterday" has a few gauges only
            continue
        old = qual.get(dd, (0, 0))
        if q[0] > old[0] or (q[0] == old[0] and q[1] >= old[1] / 2):
            got[dd] = {n: round(v, 1) for n, v in vals.items() if v is not None}
            qual[dd] = q
    for dd, vals in got.items():
        for n, v in vals.items():
            if n in past and dd in past[n]:
                past[n][dd] = v
    return got, qual

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
# anchor the river to the latest discharge below the Chao Phraya Dam (ThaiWater C.13) when it is fresh
c13 = next((r for r in live.get('river', []) if r.get('code') == 'C.13' and r.get('q')), None)
if c13 and (c13.get('time') or '')[:10] in gq and abs((date.fromisoformat(c13['time'][:10]) - TODAY).days) <= 1:
    RIVER.update(ref_date=c13['time'][:10], q_obs=c13['q'])

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

# ---------------- super-ensemble: every system we can reach ----------------
ENS_SYSTEMS = [  # Open-Meteo ensemble model id, label, weight of the whole system
    ('ecmwf_ifs025', 'ECMWF ENS', 0.24), ('ecmwf_aifs025', 'ECMWF AIFS ENS', 0.16), ('gfs05', 'NOAA GEFS', 0.11),
    ('gem_global', 'ECCC GEPS', 0.07), ('icon_seamless', 'DWD ICON-EPS', 0.07),
    ('ukmo_global_ensemble_20km', 'UKMO MOGREPS-G', 0.07),
]
DET_SYSTEMS = [  # deterministic runs, each counted as one weighted member
    ('ecmwf_ifs', 'ECMWF HRES 9 км', 0.06), ('ecmwf_aifs025_single', 'ECMWF AIFS', 0.04), ('gfs_global', 'NOAA GFS', 0.03),
    ('icon_global', 'DWD ICON', 0.03), ('jma_gsm', 'JMA GSM', 0.03), ('gem_global', 'ECCC GEM', 0.02),
    ('meteofrance_arpege_world', 'Météo-France ARPEGE', 0.02), ('ukmo_global_deterministic_10km', 'UKMO 10 км', 0.03),
    ('cma_grapes_global', 'CMA GRAPES', 0.02),
]

mats = {m: member_matrix(m) for m, _, _ in ENS_SYSTEMS if m in ens and ens[m].get('C', {}).get('members')}
ext_pool = np.concatenate([mats[m] for m in ('gfs05', 'gem_global') if m in mats], axis=0)

det = json.load(open('det_zones.json')) if os.path.exists('det_zones.json') else {}
def det_matrix(model):
    """array [zones, NF] aligned to TODAY (NaN beyond the model's horizon) plus its past days."""
    out = np.full((len(zones), NF), np.nan); past_vals = {}
    for zi, z in enumerate(zones):
        x = det[model][z]; t = x['time']; p = x['precip'] or []
        for tt, v in zip(t, p):
            if v is None:
                continue
            if tt >= TODAY.isoformat():
                k = (date.fromisoformat(tt) - TODAY).days
                if k < NF:
                    out[zi, k] = v
            else:
                past_vals.setdefault(tt, [None] * len(zones))[zi] = v
    return out, past_vals
dets = {m: det_matrix(m) for m, _, _ in DET_SYSTEMS if m in det}

seas = None  # ECMWF seasonal ensemble (51 members), one grid point, aligned to TODAY
if os.path.exists('seasonal.json'):
    sd = json.load(open('seasonal.json'))['daily']
    keys = [k for k in sd if k.startswith('precipitation_sum')]
    if TODAY.isoformat() in sd['time']:
        i0 = sd['time'].index(TODAY.isoformat())
        seas = np.array([[np.nan if v is None else v for v in sd[k][i0:i0 + NF]] + [np.nan] * max(0, NF - len(sd[k][i0:i0 + NF])) for k in keys])

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

def filler(k, ext, sm, year):
    """rain for day k when a trace has no model value of its own (or is faded to climatology)"""
    r = rng.random()
    if ext is not None and not np.isnan(ext[0, k]) and r < 0.4:
        return ext[:, k]
    noise = np.exp(rng.normal(0, 0.35, len(zones)))
    if sm is not None and not np.isnan(sm[k]) and r < 0.7:
        return sm[k] * noise
    return analog(year, k) * noise

traces = []  # list of (weight, array [zones, NF], system id)
def extend(tr, fade=True):
    year = int(rng.integers(1991, 2026))
    ext = ext_pool[int(rng.integers(0, ext_pool.shape[0]))] if len(ext_pool) else None
    sm = seas[int(rng.integers(0, len(seas)))] if seas is not None else None
    for k in range(NF):
        w_clim = min(0.85, max(0.0, (k - 9) / 14)) if fade else 0.0  # fade to extended range after ~day 10
        if np.isnan(tr[0, k]) or rng.random() < w_clim:
            tr[:, k] = filler(k, ext, sm, year)
    return tr

for m, _, wgt in ENS_SYSTEMS:
    if m not in mats:
        continue
    M = mats[m]
    for i in range(M.shape[0]):
        traces.append((wgt / M.shape[0], extend(M[i].copy()), m))
for m, _, wgt in DET_SYSTEMS:
    if m in dets:
        traces.append((wgt, extend(dets[m][0].copy()), 'det:' + m))
W = np.array([w for w, _, _ in traces]); W = W / W.sum()
NT = len(traces)

# ---------------- live gauges (ThaiWater) ----------------
# ThaiWater "today" = rain since 07:00 of the current rain day, "yesterday" = the whole 07:00 -> 07:00 day before
# (labelled with its start date). Gauges that stopped reporting keep their last "today" value, some from 2018:
# only readings of the current rain day count.
rain_day = None  # date whose 07:00 opens the window of the "today" readings
if FETCHED:
    rain_day = (FETCHED if FETCHED.hour >= 7 else FETCHED - timedelta(days=1)).date()
    for g in live.get('rain_stations', []):
        if (g.get('ttoday') or '') < rain_day.isoformat() + ' 07:00':
            g['today'] = None
gauges = [g for g in live.get('rain_stations', []) if (g.get('prov') or '').startswith('กรุงเทพ')]
def idw(key, n, k=5):
    x, y = pos[n]
    pts = [(math.hypot((g['lon'] - x) * 0.97, g['lat'] - y), g[key]) for g in gauges if g.get(key) is not None]
    if len(pts) < 3:
        return None
    pts.sort()
    w = [1 / (d * d + 1e-5) for d, _ in pts[:k]]
    return sum(wi * v for wi, (_, v) in zip(w, pts[:k])) / sum(w)
ydates = sorted({g.get('yday_date') for g in gauges if g.get('yday') is not None and g.get('yday_date')})
obs_yday_date = ydates[-1] if ydates else None
for g in gauges:
    if g.get('yday_date') != obs_yday_date:
        g['yday'] = None
obs_today = {n: idw('today', n) for n in names}
obs_yday = {n: idw('yday', n) for n in names} if obs_yday_date else {}
# Today's rain = measured since 07:00 (before 07:00 that window belongs to yesterday) + the forecast for the
# hours left until midnight; the night before 07:00 is in the gauges' previous day.
rem_frac = max(0.0, 1 - (FETCHED.hour + FETCHED.minute / 60) / 24) if FETCHED and FETCHED.date() == TODAY else 1.0

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

gauge_days, gauge_q = apply_gauge_totals()
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

# Morning state. carry.json holds the last run's start and end storage. A new day starts from the end of the last
# run of yesterday; the news levels of this morning (obs.OBS_LEVEL with OBS_DATE = today) override it wherever
# they put a district on another level.
cd = carry.get('date') or ''
morning = carry.get('start') if cd == TODAY.isoformat() else (carry.get('end') if cd and cd < TODAY.isoformat() else None)
news_today = OBS_DATE == TODAY.isoformat()
S_obs = {}
for n in names:
    m = (morning or {}).get(n)
    if news_today:
        S_obs[n] = m if m is not None and level(m) == OBS_LEVEL[n] else S_INIT[OBS_LEVEL[n]]
    else:
        S_obs[n] = m if m is not None else S_INIT[OBS_LEVEL[n]]
# past days shown as reported (obs.OBS_HIST) or as the last run of that day saw them (carry.json)
hist_lv = {d0: lv for d0, lv in carry.get('hist', {}).items() if d0 < TODAY.isoformat()}
if cd and cd < TODAY.isoformat() and carry.get('day'):
    hist_lv[cd] = carry['day']
if OBS_DATE < TODAY.isoformat():
    hist_lv.setdefault(OBS_DATE, OBS_LEVEL)
hist_lv.update(OBS_HIST)
for n in names:
    for d0, lv in hist_lv.items():
        if d0 in hist_disp[n]:
            hist_disp[n][d0] = S_INIT[lv.get(n, 1)] * 0.95
    hist_disp[n]['2026-09-24'] = min(hist_disp[n]['2026-09-24'], 25.0)

# forecast per trace
disp_f = np.zeros((NT, len(names), NF))
rain_f = np.zeros((NT, len(names), NF))
S_end0 = np.zeros((NT, len(names)))  # storage at the end of today = tomorrow's morning state
for ti, (_, tr, _sys) in enumerate(traces):
    Sx = dict(S_obs); APx = dict(API_hist)
    zn = rng.normal(0, 1, (len(zones), NF)); dn = rng.normal(0, 1, (len(names), NF))
    for k in range(NF):
        d0 = ds[T0 + k]
        for i, n in enumerate(names):
            base = float(np.dot(wz[n], np.nan_to_num(tr[:, k])))
            noise = math.exp(0.30 * zn[zones.index(zone_of[n]), k] + 0.45 * dn[i, k] - (0.30 ** 2 + 0.45 ** 2) / 2)
            rain_f[ti, i, k] = base * noise
            if k == 0 and obs_today.get(n) is not None:  # measured so far + forecast for the hours left
                rain_f[ti, i, k] = (obs_today[n] if rain_day == TODAY else 0.0) + rem_frac * rain_f[ti, i, k]
        for i, n in enumerate(names):
            APx[n] = APx[n] * 0.85 + rain_f[ti, i, k]
        cityAPI = float(np.mean(list(APx.values())))
        regAPI = float(np.mean([APx[n] for n in names if D[n]['zone'] in ('east', 'outer')]))
        for i, n in enumerate(names):
            Sx[n], disp = step(n, Sx[n], APx[n], rain_f[ti, i, k], regAPI, cityAPI, d0)
            disp_f[ti, i, k] = disp
        if k == 0:
            S_end0[ti] = [Sx[n] for n in names]
    if news_today:  # today = reported morning state + today's rain: never below the reported level
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

# ---------------- aggregation for the page: every source side by side ----------------
AGG_BACK, AGG_DAYS = 2, 16  # columns: 2 past days + 16 forecast days
cols = [(TODAY + timedelta(k)).isoformat() for k in range(-AGG_BACK, AGG_DAYS)]
wa = np.array([area[n] for n in names]) / sum(area.values())
zone_city_w = sum(wa[i] * wz[n] for i, n in enumerate(names))  # share of each zone in the city mean

def city_from_zones(v):
    v = np.array([np.nan if q is None else q for q in v], dtype=float)
    ok = ~np.isnan(v)
    return None if not ok.any() else float(np.sum(zone_city_w[ok] * v[ok]) / np.sum(zone_city_w[ok]))

def q3(xs):
    return [round(float(np.percentile(xs, 10)), 1), round(float(np.median(xs)), 1), round(float(np.percentile(xs, 90)), 1)]

rows = []
for m, label, wgt in ENS_SYSTEMS:
    if m not in mats:
        continue
    M = mats[m]; vals = []
    for c in cols:
        k = (date.fromisoformat(c) - TODAY).days
        cm = [x for x in (city_from_zones(M[i, :, k]) for i in range(M.shape[0])) if x is not None] if 0 <= k < NF else []
        vals.append(q3(cm) if cm else None)
    rows.append(dict(id=m, label=label, kind='ens', members=int(M.shape[0]), horizon=int(np.sum(~np.isnan(M[0, 0]))), weight=wgt, v=vals))
for m, label, wgt in DET_SYSTEMS:
    if m not in dets:
        continue
    fut, pastv = dets[m]; vals = []
    for c in cols:
        k = (date.fromisoformat(c) - TODAY).days
        x = (city_from_zones(pastv[c]) if c in pastv else None) if k < 0 else (city_from_zones(fut[:, k]) if k < NF else None)
        vals.append(None if x is None else round(x, 1))
    rows.append(dict(id=m, label=label, kind='det', members=1, horizon=int(np.sum(~np.isnan(fut[0]))), weight=wgt, v=vals))
if seas is not None:
    vals = []
    for c in cols:
        k = (date.fromisoformat(c) - TODAY).days
        col = seas[:, k][~np.isnan(seas[:, k])] if 0 <= k < NF else []
        vals.append(q3(col) if len(col) else None)
    rows.append(dict(id='seas5', label='ECMWF SEAS5', kind='seas', members=int(len(seas)), horizon=int(np.sum(~np.isnan(seas[0]))), weight=None, v=vals))

consensus = [None if (date.fromisoformat(c) - TODAY).days < 0 else
             [cr[q][(date.fromisoformat(c) - TODAY).days] for q in ('p10', 'p50', 'p90')] for c in cols]
obs_cols = []
for c in cols:
    k = (date.fromisoformat(c) - TODAY).days
    if k < 0:
        obs_cols.append(city_obs[ds.index(c)] if c in ds[:T0] else None)
    elif k == 0 and rain_day == TODAY and any(v is not None for v in obs_today.values()):
        obs_cols.append(round(float(np.average([obs_today[n] or 0 for n in names], weights=wa)), 1))
    else:
        obs_cols.append(None)
tmd = {r['date']: r['rain_pct'] for r in live.get('tmd_forecast', [])}
keep = ('code', 'label', 'name', 'level', 'prev', 'bank', 'pct', 'situation', 'time', 'q', 'amphoe')
agg = dict(
    cols=cols, rows=rows, consensus=consensus, obs=obs_cols, tmd=[tmd.get(c) for c in cols],
    stations=[[round(g['lon'], 4), round(g['lat'], 4), g.get('r24'), g.get('today'), g.get('name') or '', g.get('agency') or '']
              for g in live.get('rain_stations', []) if g.get('r24') is not None or g.get('today') is not None],
    gauges=dict(river=[{k: r.get(k) for k in keep} for r in live.get('river', [])],
                canals=[{k: r.get(k) for k in keep} for r in live.get('canals', [])], dams=live.get('dams', [])),
    tmd_obs=live.get('tmd_obs', []), metar=live.get('metar', []), status=live.get('status', {}),
    fetched=live.get('fetched'), tmd_built=live.get('tmd_forecast_built'),
    n=dict(r24=sum(1 for g in gauges if g.get('r24') is not None), today=sum(1 for g in gauges if g.get('today') is not None),
           yday=sum(1 for g in gauges if g.get('yday') is not None)),
    yday_date=obs_yday_date,
    yday_city=round(float(np.mean([g['yday'] for g in gauges if g.get('yday') is not None])), 1) if any(g.get('yday') is not None for g in gauges) else None,
    ntr=NT,
)

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
    agg=agg,
)
json.dump(out, open('model_out.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(dict(date=TODAY.isoformat(), fetched=live.get('fetched'), news=news_today,
               start={n: round(S_obs[n], 1) for n in names},
               end={n: round(float(wquant(S_end0[:, i:i + 1], 0.5)[0]), 1) for i, n in enumerate(names)},
               day={n: int(out_d[n]['p50'][T0]) for n in names},
               hist={d0: hist_lv[d0] for d0 in sorted(hist_lv) if d0 >= START.isoformat()},
               rain={d0: gauge_days[d0] for d0 in sorted(gauge_days)},
               rain_q={d0: list(gauge_q[d0]) for d0 in sorted(gauge_days)}),
          open(CARRY, 'w'), ensure_ascii=False, indent=0)

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
