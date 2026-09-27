"""Live observations and official products for Bangkok -> data/obs_live.json

Sources
  ThaiWater (HII / ONWR) public API: rain gauges (last 24 h, today, yesterday), water levels
    of rivers and canals, reservoir storage.
  TMD open data API: 7-day forecast for Bangkok, today's synoptic observations.
  aviationweather.gov: METAR for Suvarnabhumi (VTBS) and Don Mueang (VTBD).

    python3 fetch_obs.py [--out DIR]
"""
import argparse, json, os, subprocess, time
from datetime import datetime, timedelta, timezone

TW = 'https://api-v3.thaiwater.net/api/v1/thaiwater30/public/'
# TMD's documented demo credentials for its open data API
TMD = 'https://data.tmd.go.th/api/{}/?uid=api&ukey=api12345&format=json'
METAR = 'https://aviationweather.gov/api/data/metar?ids=VTBS,VTBD&hours=6&format=json'
ICT = timezone(timedelta(hours=7))

# map window used by the page (lon/lat); stations outside are dropped
LON0, LON1, LAT0, LAT1 = 100.30, 100.965, 13.47, 13.975

RIVER = {  # ThaiWater old codes -> label
    'C.2': 'Накхонсаван (C.2)', 'C.13': 'Плотина Чао Прайя, ниже (C.13)', 'C.3': 'Сингбури (C.3)',
    'C.7A': 'Анг Тхонг (C.7A)', 'C.35': 'Аюттхая, Бан Пом (C.35)', 'CPY014': 'Нонтхабури, мост Нуан Чави',
    'C.12': 'Бангкок, Самсен (C.12)', 'CPY015': 'Бангкок, мост Крунгтхеп',
}
DAMS = {'ภูมิพล': 'Пхумипон', 'สิริกิติ์': 'Сирикит', 'ป่าสักชลสิทธิ์': 'Пасак Чоласит', 'แควน้อยบำรุงแดน': 'Кхвэной'}
TMD_STATIONS = {'48455': 'Бангкок (центр)', '48454': 'Порт Кхлонгтой', '48453': 'Бангна', '48456': 'Аэропорт Донмыанг',
                '48429': 'Аэропорт Суварнабхуми'}


def get_json(url, tries=4, timeout=90):
    last = None
    for k in range(tries):
        r = subprocess.run(['curl', '-sS', '--fail', '--max-time', str(timeout), url], capture_output=True)
        if r.returncode == 0:
            try:
                d = json.loads(r.stdout)
                if not (isinstance(d, dict) and d.get('error')):
                    return d
                last = d.get('reason')
            except ValueError as e:
                last = str(e)
        else:
            last = r.stderr.decode(errors='ignore')[:200]
        time.sleep(3 * (k + 1))
    raise RuntimeError(last or 'request failed')


def in_view(lat, lon):
    return lat is not None and lon is not None and LAT0 <= lat <= LAT1 and LON0 <= lon <= LON1


def num(v):
    try:
        return None if v in (None, '') else float(v)
    except (TypeError, ValueError):
        return None


def main(out):
    res, status = {}, {}
    now = datetime.now(ICT)
    res['fetched'] = now.strftime('%Y-%m-%d %H:%M')

    # --- rain gauges -----------------------------------------------------------------------
    st = {}
    try:
        for x in get_json(TW + 'rain_24h')['data']:
            s = x.get('station') or {}
            lat, lon = num(s.get('tele_station_lat')), num(s.get('tele_station_long'))
            if not in_view(lat, lon):
                continue
            g = x.get('geocode') or {}
            st[s.get('id')] = dict(name=(s.get('tele_station_name') or {}).get('th'), lat=lat, lon=lon,
                                   prov=(g.get('province_name') or {}).get('th'), amphoe=(g.get('amphoe_name') or {}).get('th'),
                                   agency=((x.get('agency') or {}).get('agency_shortname') or {}).get('en'),
                                   r24=num(x.get('rain_24h')), t24=x.get('rainfall_datetime'))
        status['thaiwater_rain24'] = 'ok'
    except Exception as e:
        status['thaiwater_rain24'] = 'error: ' + str(e)[:120]
    try:
        for x in get_json(TW + 'rain_today')['data']:
            s = x.get('station') or {}
            lat, lon = num(s.get('tele_station_lat')), num(s.get('tele_station_long'))
            if not in_view(lat, lon):
                continue
            g = x.get('geocode') or {}
            d = st.setdefault(s.get('id'), dict(name=(s.get('tele_station_name') or {}).get('th'), lat=lat, lon=lon,
                                                prov=(g.get('province_name') or {}).get('th'),
                                                amphoe=(g.get('amphoe_name') or {}).get('th'),
                                                agency=((x.get('agency') or {}).get('agency_shortname') or {}).get('en')))
            d['today'] = num(x.get('rainfall_value')); d['ttoday'] = x.get('rainfall_datetime')
        status['thaiwater_rain_today'] = 'ok'
    except Exception as e:
        status['thaiwater_rain_today'] = 'error: ' + str(e)[:120]
    yday = {}
    try:
        for x in get_json(TW + 'rain_yesterday')['data']:
            lat, lon = num(x.get('tele_station_lat')), num(x.get('tele_station_long'))
            if not in_view(lat, lon):
                continue
            yday[(round(lat, 4), round(lon, 4))] = dict(v=num(x.get('rainfall_value')), date=(x.get('rainfall_datetime') or '')[:10],
                                                        amphoe=(x.get('amphoe_name') or {}).get('th'),
                                                        prov=(x.get('province_name') or {}).get('th'),
                                                        name=(x.get('tele_station_name') or {}).get('th'))
        status['thaiwater_rain_yesterday'] = 'ok'
    except Exception as e:
        status['thaiwater_rain_yesterday'] = 'error: ' + str(e)[:120]
    for d in st.values():  # attach yesterday's total to the same gauge when coordinates match
        y = yday.pop((round(d['lat'], 4), round(d['lon'], 4)), None)
        if y:
            d['yday'] = y['v']; d['yday_date'] = y['date']
    for (lat, lon), y in yday.items():
        st[f'y{lat},{lon}'] = dict(name=y['name'], lat=lat, lon=lon, prov=y['prov'], amphoe=y['amphoe'], yday=y['v'], yday_date=y['date'])
    res['rain_stations'] = list(st.values())

    # --- rivers, canals, dams --------------------------------------------------------------
    try:
        wl = get_json(TW + 'waterlevel_load')['waterlevel_data']['data']
        river, canals = [], []
        for x in wl:
            s = x.get('station') or {}
            code = s.get('tele_station_oldcode')
            g = x.get('geocode') or {}
            row = dict(code=code, name=(s.get('tele_station_name') or {}).get('th'),
                       level=num(x.get('waterlevel_msl')), prev=num(x.get('waterlevel_msl_previous')),
                       bank=num(s.get('min_bank')), pct=num(x.get('storage_percent')),
                       situation=x.get('situation_level'), time=x.get('waterlevel_datetime'),
                       q=num(x.get('discharge')), amphoe=(g.get('amphoe_name') or {}).get('th'),
                       lat=num(s.get('tele_station_lat')), lon=num(s.get('tele_station_long')))
            if code in RIVER:
                row['label'] = RIVER[code]
                river.append(row)
            elif ((g.get('province_name') or {}).get('th') or '').startswith('กรุงเทพ'):
                canals.append(row)
        order = list(RIVER)
        res['river'] = sorted(river, key=lambda r: order.index(r['code']))
        res['canals'] = sorted(canals, key=lambda r: -(r['pct'] or 0))
        status['thaiwater_waterlevel'] = 'ok'
    except Exception as e:
        status['thaiwater_waterlevel'] = 'error: ' + str(e)[:120]
    try:
        dams = get_json(TW + 'thailand_main')['dam']['data']['data']
        res['dams'] = [dict(name=DAMS[n], pct=num(x.get('dam_storage_percent')), inflow=num(x.get('dam_inflow')),
                            release=num(x.get('dam_released')), date=x.get('dam_date'))
                       for x in dams for n in [((x.get('dam') or {}).get('dam_name') or {}).get('th', '')] if n in DAMS]
        status['thaiwater_dams'] = 'ok'
    except Exception as e:
        status['thaiwater_dams'] = 'error: ' + str(e)[:120]

    # --- TMD -------------------------------------------------------------------------------
    try:
        f = get_json(TMD.format('WeatherForecast7Days/V2'))
        for p in f['Provinces']['Province']:
            if p.get('ProvinceNameEnglish') == 'Bangkok':
                s = p['SevenDaysForecast']
                days = [datetime.strptime(d, '%d/%m/%Y').strftime('%Y-%m-%d') for d in s['ForecastDate']]
                res['tmd_forecast'] = sorted([dict(date=d, rain_pct=num(r), tmax=num(tx), tmin=num(tn), desc=de)
                                              for d, r, tx, tn, de in zip(days, s['PercentRainCover'], s['MaximumTemperature'],
                                                                           s['MinimumTemperature'], s['DescriptionThai'])],
                                             key=lambda r: r['date'])
        res['tmd_forecast_built'] = f['header'].get('LastBuildDate')
        status['tmd_forecast'] = 'ok'
    except Exception as e:
        status['tmd_forecast'] = 'error: ' + str(e)[:120]
    try:
        t = get_json(TMD.format('WeatherToday/V2'))
        res['tmd_obs'] = [dict(station=TMD_STATIONS[s['WmoStationNumber']], rain=num(s['Observation'].get('Rainfall')),
                               time=s['Observation'].get('DateTime', '')[:16], temp=num(s['Observation'].get('Temperature')))
                          for s in t['Stations']['Station'] if s.get('WmoStationNumber') in TMD_STATIONS]
        status['tmd_obs'] = 'ok'
    except Exception as e:
        status['tmd_obs'] = 'error: ' + str(e)[:120]

    # --- METAR -----------------------------------------------------------------------------
    try:
        latest = {}
        for m in get_json(METAR):
            if m.get('icaoId') not in latest:
                t = datetime.fromisoformat(m['reportTime'].replace('Z', '+00:00')).astimezone(ICT)
                latest[m['icaoId']] = dict(icao=m['icaoId'], time=t.strftime('%Y-%m-%d %H:%M'), wx=m.get('wxString') or '',
                                           temp=m.get('temp'), raw=m.get('rawOb'))
        res['metar'] = list(latest.values())
        status['metar'] = 'ok'
    except Exception as e:
        status['metar'] = 'error: ' + str(e)[:120]

    res['status'] = status
    json.dump(res, open(os.path.join(out, 'obs_live.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    print('obs_live.json:', {k: v for k, v in status.items()}, len(res.get('rain_stations', [])), 'rain gauges')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
    main(ap.parse_args().out)
