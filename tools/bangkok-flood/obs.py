# Observations as of the morning of Sat 26 Sep 2026 (ICT), compiled from BMA / DDPM / Thai media reports.
# Levels: 0 dry, 1 ponding (<10 cm), 2 streets flooded 10-30 cm, 3 homes/communities 30-60 cm, 4 >60 cm.

OBS_LEVEL = {
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

_model_cache = {}
def OBS_RAIN_FACTOR(n):
    import json
    if not _model_cache:
        _model_cache.update(json.load(open('om_district_bestmatch.json')))
    x = _model_cache[n]['daily']
    p = dict(zip(x['time'], x['precipitation_sum']))
    m = (p['2026-09-24'] or 0) + (p['2026-09-25'] or 0)
    f = 0.8 * RAIN48[n] / max(m, 1)
    return {'2026-09-24': f, '2026-09-25': f}

# Chao Phraya: BMA ~1,900 m3/s on 25 Sep; Chao Phraya Dam release 1,950 m3/s from 26 Sep (cap <=2,000);
# C.2 Nakhon Sawan peak ~2,000 m3/s around 2 Oct (RID). GloFAS relative trend used, damped by 0.5.
RIVER = dict(ref_date='2026-09-26', q_obs=1950, damp=0.5, qmin=1400, qmax=2400, a=0.05, b=0.00012, q0=1500)

NORMAL_OCT_MM = 288.7      # Bangkok Metropolis 1991-2020 normal (TMD)
ANALOG_FACTOR = 0.85       # TMD/ONWR expect October 10-20% below normal (very strong El Nino)
TIDE_SEASONAL = 0.004      # m/day rise of mean sea level in the upper Gulf through October

NOTES = {}
