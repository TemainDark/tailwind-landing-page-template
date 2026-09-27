"""Download and prepare every input of the Bangkok flood outlook.

    python3 fetch_inputs.py            # writes ./data
    python3 fetch_inputs.py --out DIR  # writes somewhere else

Sources: OpenStreetMap (Overpass mirror), geoBoundaries (neighbouring districts),
Open-Meteo (forecast, ensemble, ERA5 archive, GloFAS flood, marine sea level, elevation).
Needs: pip install shapely numpy utide
"""
import argparse, json, math, os, random, subprocess, time, urllib.parse, urllib.request
from datetime import date

import numpy as np
from shapely.geometry import LineString, Point, box, shape
from shapely.ops import linemerge, polygonize, polylabel, unary_union
from shapely.prepared import prep

OVERPASS = 'https://overpass.kumi.systems/api/interpreter'
GEOB = ('https://media.githubusercontent.com/media/wmgeolab/geoBoundaries/9469f09/releaseData/'
        'gbOpen/THA/ADM2/geoBoundaries-THA-ADM2_simplified.geojson')
UA = {'User-Agent': 'bkk-flood-map/1.0'}
# OSM relations of Bangkok's 50 khet (admin_level 6 inside relation 92277)
DISTRICT_RELATIONS = ('92053,92056,92058,92061,92063,92064,92068,92069,1639285,1639286,1639287,1639288,'
                      '2938030,2938031,2938032,2938033,2938034,2938035,2938036,2939952,2939953,2939954,2939955,'
                      '2939956,2942281,2942282,2942283,2946804,2946805,2946806,2946807,2997412,3146412,3146413,'
                      '3146414,3146415,3146642,3146643,3147007,3147008,3147104,3147280,3147281,3147312,3147313,'
                      '3147425,3147455,3147456,3147500,3147501')

# map frame (lon/lat) and projection shared with the page
LON0, LON1, LAT0, LAT1 = 100.30, 100.965, 13.47, 13.975
COS = math.cos(math.radians(13.72))
K = 1000 / ((LON1 - LON0) * COS)
DET_MODELS = ['ecmwf_ifs', 'ecmwf_aifs025_single', 'gfs_global', 'icon_global', 'jma_gsm', 'gem_global',
              'meteofrance_arpege_world', 'ukmo_global_deterministic_10km', 'cma_grapes_global']
ZONES = {'C': (13.745, 100.535), 'N': (13.88, 100.60), 'E': (13.80, 100.80),
         'SE': (13.69, 100.64), 'W': (13.73, 100.40), 'S': (13.60, 100.45)}
CANALS = {'Khlong Saen Saep', 'Khlong Prawet Buri Rom', 'Khlong Phasi Charoen', 'Khlong Maha Sawat',
          'Khlong Sam Wa', 'Khlong Hok Wa', 'Khlong Prem Prachakon', 'Khlong Lat Phrao', 'Khlong Bang Sue',
          'Khlong Phra Khanong', 'Khlong Tan', 'Khlong Samrong', 'Khlong Lat Krabang', 'Khlong Bangkok Noi',
          'Khlong Bangkok Yai', 'Khlong Dan', 'Khlong Sanam Chai', 'Khlong Bang Na', 'Khlong Chak Phra',
          'Khlong Mon', 'Thawi Watthana Canal', 'Khlong Bang Khen', 'Khlong Bang Bua', 'Khlong Song',
          'Khlong Nueng', 'Khlong Kum', 'Khlong Chan', 'Khlong Sip Si', 'Khlong Nong Chok', 'Khlong Toei',
          'Khlong Phadung Krung Kasem', 'Khlong Rop Krung', 'Khlong Bang Luang', 'Khlong Ratchamontri',
          'Khlong Bang Mot'}


def get(url, data=None, timeout=240, tries=4):
    for k in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, data=data, headers=UA), timeout=timeout).read()
        except Exception:
            if k == tries - 1:
                break
            time.sleep(2 ** (k + 1))
    # some proxies drop long urllib requests; curl usually gets through
    cmd = ['curl', '-sS', '--fail', '--max-time', str(timeout), '-A', UA['User-Agent'], url]
    if data is not None:
        cmd[1:1] = ['--data-binary', '@-']
    return subprocess.run(cmd, input=data, capture_output=True, check=True).stdout


def get_json(url, tries=5, **params):
    # Open-Meteo answers {"error": true, "reason": "The service is overloaded"} under load: back off and retry
    for k in range(tries):
        d = json.loads(get(url + ('?' + urllib.parse.urlencode(params) if params else '')))
        if not (isinstance(d, dict) and d.get('error')):
            return d
        if k == tries - 1:
            raise RuntimeError(d.get('reason'))
        time.sleep(5 * (k + 1))


def overpass(q):
    return json.loads(get(OVERPASS, urllib.parse.urlencode({'data': q}).encode(), timeout=360))


def P(x, y):
    return ((x - LON0) * COS * K, (LAT1 - y) * K)


def _path(coords, close):
    pts = [P(x, y) for x, y in coords]
    s = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    px, py = round(pts[0][0], 1), round(pts[0][1], 1)
    for x, y in (pts[1:-1] if close else pts[1:]):
        x, y = round(x, 1), round(y, 1)
        dx, dy = round(x - px, 1), round(y - py, 1)
        if dx or dy:
            s += f"l{dx:g} {dy:g}"
            px, py = x, y
    return s + ('z' if close else '')


def poly_path(g):
    polys = [q for q in getattr(g, 'geoms', [g]) if q.geom_type == 'Polygon']
    out = ''
    for p in polys:
        if p.area < 2e-7:
            continue
        out += _path(list(p.exterior.coords), True)
        for r in p.interiors:
            out += _path(list(r.coords), True)
    return out


def line_path(g):
    return ''.join(_path(list(l.coords), False) for l in getattr(g, 'geoms', [g])
                   if l.geom_type == 'LineString' and len(l.coords) > 1)


def merge(lines):
    u = unary_union(lines)
    return linemerge(u) if u.geom_type == 'MultiLineString' else u


def build_geo(out):
    print('OSM districts ...')
    rel = overpass(f'[out:json][timeout:300];rel(id:{DISTRICT_RELATIONS});out geom;')
    shapes, thai = {}, {}
    for e in rel['elements']:
        en = e['tags'].get('name:en', '').replace(' District', '')
        lines = [LineString([(p['lon'], p['lat']) for p in m['geometry']]) for m in e.get('members', [])
                 if m['type'] == 'way' and m.get('role') in ('outer', '') and 'geometry' in m]
        shapes[en] = unary_union(list(polygonize(unary_union(lines))))
        thai[en] = e['tags'].get('name')
    assert len(shapes) == 50, len(shapes)
    bkk = unary_union(list(shapes.values()))
    view = box(100.27, 13.44, 101.00, 14.00)

    print('geoBoundaries neighbours ...')
    gb = json.loads(get(GEOB))
    nb = []
    for f in gb['features']:
        g = shape(f['geometry'])
        if not g.intersects(view) or bkk.buffer(0.001).contains(g.representative_point()):
            continue
        gi = g.intersection(view).difference(bkk.buffer(0.0005))
        if gi.area > 1e-5:
            nb.append({'en': f['properties']['shapeName'], 'd': poly_path(gi.simplify(0.0006, preserve_topology=True))})

    print('OSM waterways ...')
    w = overpass('[out:json][timeout:180];(way["waterway"="river"](13.45,100.28,14.00,100.98);'
                 'way["waterway"="canal"]["name"](13.45,100.28,14.00,100.98););out tags geom;')
    river, canals = [], {}
    for e in w['elements']:
        t = e.get('tags', {}); nm = t.get('name:en') or t.get('name') or ''
        ls = LineString([(p['lon'], p['lat']) for p in e['geometry']])
        if t.get('waterway') == 'river' and nm == 'Chao Phraya River':
            river.append(ls)
        elif nm in CANALS:
            canals.setdefault(nm, []).append(ls)
    rv = merge(river).intersection(view)
    can = {k: merge(v).intersection(bkk.buffer(0.012)) for k, v in canals.items()}

    dist = []
    for en, g in shapes.items():
        lab = polylabel(g, tolerance=0.0005); lx, ly = P(lab.x, lab.y); c = g.centroid
        dist.append({'en': en, 'th': thai[en], 'd': poly_path(g.simplify(0.00028, preserve_topology=True)),
                     'lx': round(lx, 1), 'ly': round(ly, 1), 'area': round(g.area * 111.32 * 110.57 * COS, 1),
                     'lon': round(c.x, 4), 'lat': round(c.y, 4)})
    geo = {'vb': [0, 0, 1000, round((LAT1 - LAT0) * K, 1)], 'proj': {'lon0': LON0, 'lat1': LAT1, 'cos': COS, 'k': K},
           'districts': dist, 'neighbours': nb, 'outline': poly_path(bkk.simplify(0.00028)),
           'river': line_path(rv.simplify(0.0002)),
           'canals': [{'en': k, 'd': line_path(v.simplify(0.0003))} for k, v in can.items() if v.length * 108 > 1.5]}
    json.dump(geo, open(os.path.join(out, 'geo.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    return shapes


def fetch_weather(out, pts, shapes=None):
    """pts: district -> (lon, lat); shapes (polygons) are only needed to sample the DEM the first time"""
    names = list(pts)
    print('Open-Meteo per-district rain ...')
    d = get_json('https://api.open-meteo.com/v1/forecast',
                 latitude=','.join(f'{pts[n][1]:.4f}' for n in names), longitude=','.join(f'{pts[n][0]:.4f}' for n in names),
                 daily='precipitation_sum,precipitation_probability_max,precipitation_hours',
                 past_days=21, forecast_days=16, timezone='Asia/Bangkok')
    json.dump({n: x for n, x in zip(names, d)}, open(os.path.join(out, 'om_district_bestmatch.json'), 'w'))

    print('Open-Meteo ensembles ...')
    zn = list(ZONES)
    ens = {}
    for m in ['ecmwf_ifs025', 'ecmwf_aifs025', 'gfs05', 'gem_global', 'icon_seamless', 'ukmo_global_ensemble_20km', 'gfs025']:
        d = get_json('https://ensemble-api.open-meteo.com/v1/ensemble',
                     latitude=','.join(str(ZONES[z][0]) for z in zn), longitude=','.join(str(ZONES[z][1]) for z in zn),
                     daily='precipitation_sum', models=m, forecast_days=35, timezone='Asia/Bangkok')
        ens[m] = {}
        for z, x in zip(zn, d):
            dl = x['daily']
            ens[m][z] = {'time': dl['time'], 'lat': x['latitude'], 'lon': x['longitude'],
                         'members': [dl[k] for k in dl if k.startswith('precipitation_sum')]}
    json.dump(ens, open(os.path.join(out, 'ens_zones.json'), 'w'))

    print('Open-Meteo deterministic models ...')
    det = {}
    for m in DET_MODELS:
        try:
            d = get_json('https://api.open-meteo.com/v1/forecast',
                         latitude=','.join(str(ZONES[z][0]) for z in zn), longitude=','.join(str(ZONES[z][1]) for z in zn),
                         daily='precipitation_sum', models=m, past_days=3, forecast_days=16, timezone='Asia/Bangkok')
        except Exception as e:
            print('  skip', m, e)
            continue
        det[m] = {z: {'time': x['daily']['time'], 'precip': x['daily'].get('precipitation_sum')} for z, x in zip(zn, d)}
        time.sleep(1)
    json.dump(det, open(os.path.join(out, 'det_zones.json'), 'w'))

    print('Seasonal ensemble ...')
    try:
        json.dump(get_json('https://seasonal-api.open-meteo.com/v1/seasonal', latitude=13.75, longitude=100.55,
                           daily='precipitation_sum', forecast_days=45, timezone='Asia/Bangkok'),
                  open(os.path.join(out, 'seasonal.json'), 'w'))
    except Exception as e:
        print('  seasonal unavailable:', e)

    if os.path.exists(os.path.join(out, 'era5_bkk.json')):
        print('ERA5 climatology: kept existing file (1991-2025 does not change)')
    else:
        print('ERA5 climatology ...')
        y = date.today().year - 1
        json.dump(get_json('https://archive-api.open-meteo.com/v1/archive', latitude=13.75, longitude=100.55,
                           start_date='1991-01-01', end_date=f'{y}-12-31', daily='precipitation_sum', timezone='Asia/Bangkok'),
                  open(os.path.join(out, 'era5_bkk.json'), 'w'))

    try:
        print('GloFAS river discharge ...')
        json.dump(get_json('https://flood-api.open-meteo.com/v1/flood',
                           latitude='13.74,13.86,14.02,14.35,15.16,15.68', longitude='100.50,100.50,100.53,100.57,100.18,100.12',
                           daily='river_discharge,river_discharge_mean,river_discharge_median,river_discharge_max,'
                                 'river_discharge_min,river_discharge_p25,river_discharge_p75',
                           past_days=45, forecast_days=30),
                  open(os.path.join(out, 'glofas.json'), 'w'))
        json.dump(get_json('https://flood-api.open-meteo.com/v1/flood', latitude=13.74, longitude=100.50,
                           daily='river_discharge', past_days=10, forecast_days=30, ensemble='true'),
                  open(os.path.join(out, 'glofas_ens.json'), 'w'))

        print('Sea level + harmonic tides ...')
        mar = get_json('https://marine-api.open-meteo.com/v1/marine', latitude='13.45,13.40', longitude='100.58,100.60',
                       hourly='sea_level_height_msl', past_days=10, forecast_days=16, timezone='Asia/Bangkok')
        json.dump(mar, open(os.path.join(out, 'marine.json'), 'w'))
        tides(mar[0], out)

    except Exception as e:  # keep the previous files; the model still runs
        print('  river/tide refresh failed, keeping previous files:', str(e)[:160])
    if os.path.exists(os.path.join(out, 'elev_samples.json')) or shapes is None:
        print('DEM samples: kept existing file (terrain does not change)')
        return
    print('DEM samples ...')
    random.seed(1)
    pts = []
    for n, g in shapes.items():
        x0, y0, x1, y1 = g.bounds; pg = prep(g); c = []
        while len(c) < 24:
            x, yy = random.uniform(x0, x1), random.uniform(y0, y1)
            if pg.contains(Point(x, yy)):
                c.append((n, x, yy))
        pts += c
    elev = []
    for i in range(0, len(pts), 60):
        ch = pts[i:i + 60]
        elev += get_json('https://api.open-meteo.com/v1/elevation', latitude=','.join(f'{q[2]:.4f}' for q in ch),
                         longitude=','.join(f'{q[1]:.4f}' for q in ch))['elevation']
        time.sleep(0.3)
    json.dump({'pts': pts, 'elev': elev}, open(os.path.join(out, 'elev_samples.json'), 'w'))


def tides(mar, out):
    import utide
    from utide.utilities import Bunch
    h = mar['hourly']
    t = np.array([np.datetime64(x) for x in h['time']])
    v = np.array([np.nan if x is None else x for x in h['sea_level_height_msl']])
    m = ~np.isnan(v)
    infer = Bunch(inferred_names=['P1', 'K2', 'N2', 'Q1'], reference_names=['K1', 'S2', 'M2', 'O1'],
                  amp_ratios=[0.331, 0.272, 0.194, 0.194], phase_offsets=[0, 0, 0, 0])
    coef = utide.solve(t[m], v[m], lat=13.45, method='ols', conf_int='none', trend=False, constit='auto',
                       infer=infer, verbose=False)
    t0 = t[0].astype('datetime64[D]')
    tp = np.arange(t0, t0 + np.timedelta64(46, 'D'), np.timedelta64(1, 'h')).astype('datetime64[m]')
    hp = utide.reconstruct(tp, coef, verbose=False).h
    json.dump({'hourly_t': [str(x) for x in tp], 'hourly_h': [round(float(x), 3) for x in hp], 'fit_mean': float(coef.mean)},
              open(os.path.join(out, 'tide_pred.json'), 'w'))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
    ap.add_argument('--refresh-geo', action='store_true', help='rebuild district geometry from OSM even if geo.json exists')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    have = all(os.path.exists(os.path.join(a.out, f)) for f in ('geo.json', 'elev_samples.json'))
    if a.refresh_geo or not have:
        shapes = build_geo(a.out)
        pts = {n: (g.representative_point().x, g.representative_point().y) for n, g in shapes.items()}
    else:  # geometry does not change between forecast refreshes
        print('Geometry: kept existing geo.json')
        shapes = None
        pts = {d['en']: (d['lon'], d['lat']) for d in json.load(open(os.path.join(a.out, 'geo.json')))['districts']}
    fetch_weather(a.out, pts, shapes)
    print('done ->', a.out)
