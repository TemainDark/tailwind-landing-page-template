# Observed flood levels compiled from BMA / DDPM / Thai media reports.
# Levels: 0 dry, 1 ponding (<10 cm), 2 streets flooded 10-30 cm, 3 homes/communities 30-60 cm, 4 >60 cm.

OBS_DATE = "2026-09-28"   # the morning OBS_LEVEL describes (news); later days start from carry.json

# Saturday 26 Sep, morning to midday
OBS_26 = {
    # east (hardest hit)
    "Bang Kapi": 4,        # Khlong Chan flats chest-high / ~1 m; Saen Saep overflowed at Bang Kapi junction
    "Nong Chok": 3, "Min Buri": 3, "Lat Krabang": 3, "Khlong Sam Wa": 3,
    "Khan Na Yao": 3, "Suan Luang": 3,
    "Prawet": 2, "Wang Thonglang": 2, "Bueng Kum": 2, "Saphan Sung": 2,
    # north
    "Chatuchak": 3,        # Vibhavadi ~30 cm (1 m at shoulder), Phong Phet, Sena Nikhom no-go
    "Bang Khen": 3,        # Bang Bua 30-50 cm, spots >1 m
    "Lak Si": 3,           # Chaeng Watthana ~50 cm, closed
    "Don Mueang": 2, "Sai Mai": 2, "Lat Phrao": 2, "Bang Sue": 1,
    # Sukhumvit / centre
    "Vadhana": 2,          # Sukhumvit 63 (Ekkamai) no-go
    "Phra Khanong": 2, "Huai Khwang": 2, "Din Daeng": 2, "Phaya Thai": 2,
    "Khlong Toei": 1, "Bang Na": 1, "Ratchathewi": 1, "Pathum Wan": 1, "Bang Rak": 1, "Sathon": 1,
    "Phra Nakhon": 1, "Samphanthawong": 1, "Pom Prap Sattru Phai": 1, "Dusit": 1,
    "Bang Kho Laem": 1, "Yan Nawa": 1,
    # west (Thonburi side "mostly normal" at 09:50)
    "Bang Khun Thian": 1, "Bang Bon": 1,
    "Thawi Watthana": 0, "Taling Chan": 0, "Bang Khae": 0, "Nong Khaem": 0, "Phasi Charoen": 0,
    "Chom Thong": 0, "Bangkok Yai": 0, "Bangkok Noi": 0, "Bang Phlat": 0, "Thon Buri": 0,
    "Khlong San": 0, "Rat Burana": 0, "Thung Khru": 0,
}

# Monday 28 Sep, morning to ~09:30. A thunderstorm over Suvarnabhumi at 01-04 h: in the 24 h to 07:00 up to 63 mm
# at the Saen Saep sluice (Nong Chok), 46.5 mm overnight in Lat Krabang, TMD Suvarnabhumi 48.8 mm. BMA (evening
# 27 Sep): 44 flooded road points on 29 roads. Khlong Chan ~1.5 m, Kheha Romklao >1 m. BMA expects Sai Mai, Khlong
# Chan, Kheha Romklao and Khu Bon to start receding today and all areas back to normal by 1 Oct (Kheha Romklao
# ~7 days). Levels start from the state carried over from 27 Sep (carry.json) and follow the reports where they differ.
OBS_LEVEL = {
    "Bang Kapi": 4,        # Khlong Chan flats ~1.5 m, power cut overnight; NIDA junction down ~10 cm (Thai PBS 07:26)
    "Lat Krabang": 4,      # Kheha Romklao >1 m, no power; the slowest area to drain, ~7 days (BMA via Thai PBS)
    "Min Buri": 3, "Nong Chok": 3, "Khlong Sam Wa": 3,   # still high; 51-63 mm overnight at the eastern sluices
    "Bang Khen": 3,        # Lat Phrao canal at Wat Bang Bua above the bank (ThaiWater 121 %)
    "Sai Mai": 3,          # BMA: starts receding today
    "Suan Luang": 2, "Bueng Kum": 2, "Don Mueang": 2,    # road sensors 15-20+ cm and falling, no community reports
    "Prawet": 2, "Khan Na Yao": 2, "Saphan Sung": 2, "Wang Thonglang": 2, "Lat Phrao": 2, "Chatuchak": 2,
    "Lak Si": 2,           # Vibhavadi open to all vehicles from 06:30, side sois still high
    "Huai Khwang": 2,      # Phetchaburi Rd at Khlong Tan still high; flooded points in Huai Khwang/Watthana 16 -> 3 on 27 Sep
    "Phra Khanong": 1, "Bang Na": 1, "Ratchathewi": 1, "Vadhana": 1,
    "Khlong Toei": 0, "Din Daeng": 0, "Phaya Thai": 0, "Bang Sue": 0, "Thawi Watthana": 0, "Bang Khun Thian": 0,
    "Bang Khae": 0, "Pathum Wan": 0, "Bang Rak": 0, "Sathon": 0, "Phra Nakhon": 0, "Samphanthawong": 0,
    "Pom Prap Sattru Phai": 0, "Dusit": 0, "Bang Kho Laem": 0, "Yan Nawa": 0, "Taling Chan": 0, "Nong Khaem": 0,
    "Phasi Charoen": 0, "Chom Thong": 0, "Bangkok Yai": 0, "Bangkok Noi": 0, "Bang Phlat": 0, "Thon Buri": 0,
    "Khlong San": 0, "Rat Burana": 0, "Thung Khru": 0, "Bang Bon": 0,
}

# Sunday 27 Sep, morning to ~11:00: rain eased (BMA 24-h max 85 mm to 07:00), 39 of 80 road points still
# flooded, east communities still deep, four trunk canals at red level. (The page shows 27 Sep as the last model
# run of that day saw it, carry.json.)
OBS_27 = {
    "Bang Kapi": 4,        # Khlong Chan flats ~1 m, waist-deep in places
    "Lat Krabang": 4,      # Kheha Romklao knee- to chest-deep, shoulder-high spots, power cut
    "Min Buri": 3, "Nong Chok": 3, "Khlong Sam Wa": 3, "Suan Luang": 3, "Bueng Kum": 3,
    "Bang Khen": 3, "Sai Mai": 3, "Don Mueang": 3,
    "Prawet": 2, "Khan Na Yao": 2, "Saphan Sung": 2, "Wang Thonglang": 2, "Chatuchak": 2, "Lak Si": 2,
    "Lat Phrao": 2, "Phra Khanong": 2, "Bang Na": 2, "Huai Khwang": 2, "Ratchathewi": 2,
    "Vadhana": 1, "Khlong Toei": 1, "Din Daeng": 1, "Phaya Thai": 1, "Bang Sue": 1,
    "Thawi Watthana": 1, "Bang Khun Thian": 1, "Bang Khae": 1,
    "Pathum Wan": 0, "Bang Rak": 0, "Sathon": 0, "Phra Nakhon": 0, "Samphanthawong": 0,
    "Pom Prap Sattru Phai": 0, "Dusit": 0, "Bang Kho Laem": 0, "Yan Nawa": 0,
    "Taling Chan": 0, "Nong Khaem": 0, "Phasi Charoen": 0, "Chom Thong": 0, "Bangkok Yai": 0,
    "Bangkok Noi": 0, "Bang Phlat": 0, "Thon Buri": 0, "Khlong San": 0, "Rat Burana": 0,
    "Thung Khru": 0, "Bang Bon": 0,
}

# Friday 25 Sep (reports through the day and evening)
OBS_25 = {
    "Nong Chok": 3, "Suan Luang": 3, "Khan Na Yao": 3,               # declared disaster zones on 25 Sep
    "Min Buri": 2, "Lat Krabang": 2, "Khlong Sam Wa": 2, "Sai Mai": 2, "Lak Si": 2, "Bang Kapi": 2,
    "Wang Thonglang": 2, "Bueng Kum": 2, "Prawet": 2, "Bang Na": 2, "Bang Khen": 2, "Chatuchak": 2,
    "Huai Khwang": 1, "Phra Khanong": 1, "Saphan Sung": 1, "Don Mueang": 1, "Lat Phrao": 1,
    "Vadhana": 1, "Din Daeng": 1, "Phaya Thai": 1,
}

# Approx. 48-h rain totals (16:00 24 Sep -> 06:00 26 Sep), mm. Station values from BMA reports for
# Min Buri 274.5, Khlong Sam Wa 273.0, Chatuchak 210 (24 h), Wang Thonglang 205.5 (24 h), Saphan Sung 203.5 (24 h),
# Phaya Thai 203.0 (24 h), Huai Khwang 201.0 (24 h); others interpolated. 80% assigned to model days 24-25 Sep.
RAIN48 = {
    "Min Buri": 275, "Khlong Sam Wa": 273, "Saphan Sung": 260, "Nong Chok": 230, "Lat Krabang": 220,
    "Khan Na Yao": 250, "Bueng Kum": 240, "Bang Kapi": 250, "Suan Luang": 220, "Prawet": 200,
    "Sai Mai": 230, "Bang Khen": 240, "Lak Si": 230, "Don Mueang": 220, "Wang Thonglang": 245,
    "Lat Phrao": 240, "Chatuchak": 250, "Huai Khwang": 240, "Din Daeng": 230, "Phaya Thai": 240,
    "Bang Sue": 210, "Ratchathewi": 210, "Dusit": 190, "Vadhana": 210, "Khlong Toei": 190,
    "Phra Khanong": 200, "Bang Na": 190, "Pathum Wan": 200, "Bang Rak": 180, "Sathon": 180,
    "Phra Nakhon": 170, "Pom Prap Sattru Phai": 180, "Samphanthawong": 175, "Yan Nawa": 170,
    "Bang Kho Laem": 165, "Bang Phlat": 150, "Bangkok Noi": 140, "Bangkok Yai": 130, "Thon Buri": 130,
    "Khlong San": 140, "Taling Chan": 140, "Thawi Watthana": 140, "Bang Khae": 130, "Nong Khaem": 130,
    "Phasi Charoen": 130, "Chom Thong": 130, "Rat Burana": 140, "Thung Khru": 140, "Bang Bon": 120,
    "Bang Khun Thian": 120,
}

OBS_26_PEAK = dict(OBS_26, **{"Lat Krabang": 4, "Bueng Kum": 3, "Thawi Watthana": 2})  # evening reports of 26 Sep
OBS_HIST = {"2026-09-25": OBS_25, "2026-09-26": OBS_26_PEAK}

# Rain 07:00 26 Sep -> 07:00 27 Sep (BMA: Sai Mai 85, Nong Chok 83, Don Mueang 71 mm; "moderate to heavy");
# other districts estimated. Calendar day 26 Sep = 20% of RAIN48 (00-06 h) + 70% of this window.
RAIN_2627 = {
    "Sai Mai": 85, "Nong Chok": 83, "Don Mueang": 71, "Khlong Sam Wa": 70, "Min Buri": 60, "Bang Khen": 60,
    "Lak Si": 55, "Lat Krabang": 50, "Khan Na Yao": 50, "Bueng Kum": 45, "Saphan Sung": 40, "Bang Kapi": 40,
    "Lat Phrao": 40, "Chatuchak": 40, "Wang Thonglang": 35, "Prawet": 35, "Suan Luang": 35, "Bang Na": 30,
    "Phra Khanong": 30, "Huai Khwang": 30, "Din Daeng": 30, "Phaya Thai": 30, "Bang Sue": 30, "Vadhana": 25,
    "Khlong Toei": 25, "Ratchathewi": 25, "Pathum Wan": 25, "Dusit": 25, "Bang Rak": 20, "Sathon": 20,
    "Phra Nakhon": 20, "Pom Prap Sattru Phai": 20, "Samphanthawong": 20, "Yan Nawa": 20, "Bang Kho Laem": 20,
    "Bang Phlat": 20, "Bangkok Noi": 20, "Taling Chan": 20, "Thawi Watthana": 20, "Bangkok Yai": 18,
    "Thon Buri": 18, "Khlong San": 18, "Bang Khae": 18, "Nong Khaem": 18, "Phasi Charoen": 18, "Chom Thong": 18,
    "Rat Burana": 18, "Thung Khru": 18, "Bang Bon": 15, "Bang Khun Thian": 15,
}

_model_cache = {}
def OBS_RAIN_FACTOR(n):
    import json
    if not _model_cache:
        _model_cache.update(json.load(open('om_district_bestmatch.json')))
    x = _model_cache[n]['daily']
    p = dict(zip(x['time'], x['precipitation_sum']))
    m = (p['2026-09-24'] or 0) + (p['2026-09-25'] or 0)
    f = 0.8 * RAIN48[n] / max(m, 1)
    f26 = (0.2 * RAIN48[n] + 0.7 * RAIN_2627[n]) / max(p.get('2026-09-26') or 0, 1)
    return {'2026-09-24': f, '2026-09-25': f, '2026-09-26': f26}

# Chao Phraya: Chao Phraya Dam release 1,950 m3/s (27 Sep, ONWR); RID may raise it to 2,000-2,300 m3/s,
# peak flow expected 27-29 Sep; C.2 Nakhon Sawan 1,846 m3/s. GloFAS relative trend used, damped by 0.5.
RIVER = dict(ref_date='2026-09-27', q_obs=1950, damp=0.5, qmin=1400, qmax=2500, a=0.05, b=0.00012, q0=1500)

NORMAL_OCT_MM = 288.7      # Bangkok Metropolis 1991-2020 normal (TMD)
ANALOG_FACTOR = 0.85       # TMD/ONWR expect October 10-20% below normal (very strong El Nino)
TIDE_SEASONAL = 0.004      # m/day rise of mean sea level in the upper Gulf through October

NOTES = {}
