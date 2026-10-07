# Observed flood levels compiled from BMA / DDPM / Thai media reports.
# Levels: 0 dry, 1 ponding (<10 cm), 2 streets flooded 10-30 cm, 3 homes/communities 30-60 cm, 4 >60 cm.

OBS_DATE = "2026-10-07"   # the morning OBS_LEVEL describes (news); later days start from carry.json

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

# Wednesday 7 Oct, morning to ~07:20. On 6 Oct midday storms (up to 42 mm/h around 10:45): 70 mm at the TMD Khlong
# Toei Port gauge (24 h to 19:00), 49 mm at Lam Pla Thio (Lat Krabang), 35 mm at Suvarnabhumi; showers 22:30-02:00.
# Floodboard roads with water peaked at 152 km (12:35), 28 km at 05:28 and 43 km at 07:17 (2.7 km impassable), mostly
# in Lat Krabang. TMD warning No. 1 of a new series (7 Oct): heavy to very heavy rain 9-13 Oct, Bangkok 10-12 Oct.
# Citizen reports are unverified. Levels start from the state carried over from 6 Oct (carry.json).
OBS_LEVEL = {
    "Lat Krabang": 3,      # 9.9 km wet (2.1 km on 6 Oct), Pracha Phatthana Rd 70 cm, "worsening"; Lam Pla Thio canal at its bank (corrected from 2)
    "Min Buri": 3,         # max 60 cm, 6.3 km wet (1.8 km on 6 Oct); Sihaburanukit sensor 5 cm (corrected from 2)
    "Khlong Sam Wa": 2,    # Floodboard "severe": 80 cm on 1.3 km (corrected from 0)
    "Nong Chok": 2,        # max 45 cm, 2.2 km, stable
    "Saphan Sung": 2,      # max 45 cm, 3.8 km, stable
    "Sai Mai": 2,          # max 50 cm, 2.0 km, improving (corrected from 0)
    "Bang Kapi": 2,        # max 40 cm, 1.7 km, improving (corrected from 1)
    "Suan Luang": 2,       # 9.5 km of shallow water, max 30 cm; Phatthanakan sensor 7.6 cm (corrected from 0)
    "Prawet": 1,           # 0.8 km, max 40 cm (corrected from 2)
    "Bang Khen": 1,        # 0.8 km, 45 cm, 0.6 km impassable (corrected from 0)
    "Bueng Kum": 1,        # 0.8 km, 37 cm (corrected from 0)
    "Khan Na Yao": 1,      # 1.2 km, 25 cm, Suan Siam Rd impassable (corrected from 0)
    "Lat Phrao": 1,        # 0.5 km wet
    "Phra Khanong": 1,     # 0.3 km at Wachirathammasathit Soi 25, depth not given (corrected from 0)
    "Huai Khwang": 0, "Don Mueang": 0, "Din Daeng": 0, "Vadhana": 0, "Khlong Toei": 0,   # dry this morning
    "Wang Thonglang": 0, "Lak Si": 0, "Chatuchak": 0, "Bang Bon": 0, "Bang Phlat": 0, "Taling Chan": 0,
    "Thawi Watthana": 0, "Bang Sue": 0, "Bang Na": 0, "Thung Khru": 0, "Phaya Thai": 0, "Ratchathewi": 0,
    "Bangkok Yai": 0, "Bang Khun Thian": 0, "Bang Khae": 0, "Dusit": 0, "Phra Nakhon": 0, "Bang Kho Laem": 0,
    "Yan Nawa": 0, "Bangkok Noi": 0, "Khlong San": 0, "Thon Buri": 0, "Bang Rak": 0, "Pathum Wan": 0,
    "Pom Prap Sattru Phai": 0, "Samphanthawong": 0, "Sathon": 0, "Phasi Charoen": 0, "Nong Khaem": 0,
    "Rat Burana": 0, "Chom Thong": 0,
}

# Tuesday 6 Oct, morning to ~07:15. On 5 Oct storms over the city (TMD warning No. 9: thunderstorms over 80% of
# Bangkok on 5-6 Oct): Floodboard roads with water peaked at 131 km (13:20), 20 km at 06:26, 30 km at 07:11 (2.5 km
# impassable). Overnight burst to ~05:00 (up to 57 mm/h): 24 h to 06:00 106 mm at Khlong Lat Phrao, 53 Don Mueang,
# 52 Asok, 50 Khlong Toei; the east got 1-17 mm. Citizen reports are unverified. Levels start from the state
# carried over from 5 Oct (carry.json).
OBS_06 = {
    "Lat Krabang": 2,      # max 70 cm, most sois 10-25 cm, 2.1 km wet (10.5 km on 5 Oct); Khlong Lam Pla Thio at 99.8% of bank (corrected from 3)
    "Prawet": 2,           # max 35 cm, 2.0 km, improving (corrected from 3)
    "Min Buri": 2,         # max 45 cm, 1.8 km (0.4 impassable), stable
    "Nong Chok": 2,        # max 50 cm, 1.6 km, stable
    "Bang Kapi": 2,        # Floodboard "severe": 2.5 km, spots to 80 cm after 33 mm overnight (corrected from 0)
    "Saphan Sung": 2,      # 3.5 km wet, 45 cm (corrected from 1)
    "Lat Phrao": 2,        # 106 mm at Khlong Lat Phrao overnight, 2.5 km wet (corrected from 0)
    "Huai Khwang": 2,      # 2.1 km wet, Soi Phetchaburi 47 Yaek 3 40 cm and impassable (corrected from 0)
    "Vadhana": 1,          # 52 mm at Asok; 0.8 km, 25 cm, Ekkamai 26 and Sukhumvit 63 impassable at 03:00 (corrected from 0)
    "Don Mueang": 1,       # 53 mm overnight, Phahon Yothin 73 0.2 km impassable (corrected from 0)
    "Suan Luang": 1,       # 0.1 km, under 10 cm (7 km on 5 Oct)
    "Phra Khanong": 0,     # Bang Chak dry, no active reports
    "Khlong Sam Wa": 0, "Bueng Kum": 0, "Bang Khen": 0, "Wang Thonglang": 0, "Sai Mai": 0, "Lak Si": 0, "Chatuchak": 0,
    "Khan Na Yao": 0, "Bang Bon": 0, "Din Daeng": 0, "Bang Phlat": 0, "Taling Chan": 0, "Thawi Watthana": 0, "Bang Sue": 0,
    "Bang Na": 0, "Thung Khru": 0, "Phaya Thai": 0, "Ratchathewi": 0, "Bangkok Yai": 0, "Bang Khun Thian": 0, "Bang Khae": 0,
    "Dusit": 0, "Phra Nakhon": 0, "Bang Kho Laem": 0, "Yan Nawa": 0, "Bangkok Noi": 0, "Khlong San": 0, "Thon Buri": 0,
    "Bang Rak": 0, "Pathum Wan": 0, "Pom Prap Sattru Phai": 0, "Samphanthawong": 0, "Sathon": 0, "Khlong Toei": 0,
    "Phasi Charoen": 0, "Nong Khaem": 0, "Rat Burana": 0, "Chom Thong": 0,
}

# Monday 5 Oct, morning to ~07:20. On 4 Oct afternoon storms in 22 districts (BMA: up to 42.5 mm in Suan Luang), 38 mm
# at Bang Kapi in 24 h; Floodboard roads with water peaked at 131 km (15:31), 38 km at 07:10 (5.5 km impassable).
# Citizen reports are unverified. Levels start from the state carried over from 4 Oct (carry.json).
OBS_05 = {
    "Lat Krabang": 3,      # 30-60 cm, sois to 80 cm, 10.5 km wet, Chao Khun Thahan 3.7 km impassable; Floodboard "severe"
    "Nong Chok": 3,        # 30-60 cm, some 60+; "severe, stable"
    "Min Buri": 3,         # 30-60 cm (max 50)
    "Prawet": 3,           # 30-60 cm (max 45), 5.2 km wet (corrected from 2)
    "Saphan Sung": 2,      # reports to 80 cm on 1.1 km (corrected from 1)
    "Suan Luang": 2,       # 10-30 cm, 7 km wet after 42.5 mm on 4 Oct (corrected from 0)
    "Bueng Kum": 1, "Bang Kapi": 1, "Lat Phrao": 1, "Bang Khen": 1, "Wang Thonglang": 1, "Khlong Sam Wa": 1,
    "Don Mueang": 1,       # spots after the 4 Oct storms
    "Sai Mai": 0, "Lak Si": 0, "Huai Khwang": 0, "Chatuchak": 0, "Khan Na Yao": 0, "Phra Khanong": 0, "Bang Bon": 0,
    "Din Daeng": 0, "Bang Phlat": 0, "Taling Chan": 0, "Thawi Watthana": 0, "Bang Sue": 0, "Bang Na": 0, "Thung Khru": 0,
    "Phaya Thai": 0, "Vadhana": 0, "Ratchathewi": 0, "Bangkok Yai": 0, "Bang Khun Thian": 0, "Bang Khae": 0, "Dusit": 0,
    "Phra Nakhon": 0, "Bang Kho Laem": 0, "Yan Nawa": 0, "Bangkok Noi": 0, "Khlong San": 0, "Thon Buri": 0, "Bang Rak": 0,
    "Pathum Wan": 0, "Pom Prap Sattru Phai": 0, "Samphanthawong": 0, "Sathon": 0, "Khlong Toei": 0, "Phasi Charoen": 0,
    "Nong Khaem": 0, "Rat Burana": 0, "Chom Thong": 0,
}

# Sunday 4 Oct, morning to ~07:30. On 3 Oct afternoon storms (peak ~43 mm/h around 14:00; 18 mm Lat Krabang, 15 mm
# Bang Khen); Floodboard roads with water peaked at 167 km (12:39) and were 42 km at 07:18 (3.5 km impassable). Citizen
# reports are unverified. Levels start from the state carried over from 3 Oct (carry.json).
OBS_04 = {
    "Lat Krabang": 3,      # Floodboard "severe", Mubaan Sirithon soi ~80 cm; Chao Khun Thahan sensor 5 cm; area flat
    "Nong Chok": 3,        # 30-60 cm, Khlong 13 road 45 cm; "significant, stable"
    "Prawet": 3,           # 45 cm spots, stable
    "Min Buri": 3,         # Rat Uthit Rd 45 cm, "significant, stable" (corrected from 2)
    "Saphan Sung": 2,      # 45 cm spots, improving
    "Khlong Sam Wa": 2,    # 45 cm spots
    "Bueng Kum": 2,        # 45 cm, 3.4 km of road with water, "significant" (corrected from 1)
    "Sai Mai": 1, "Bang Kapi": 1, "Suan Luang": 1, "Lak Si": 1, "Bang Khen": 1, "Huai Khwang": 1, "Chatuchak": 1,
    "Lat Phrao": 1, "Don Mueang": 1,   # spots after the 3 Oct storm
    "Khan Na Yao": 0, "Wang Thonglang": 0, "Phra Khanong": 0, "Bang Bon": 0, "Din Daeng": 0, "Bang Phlat": 0,
    "Taling Chan": 0, "Thawi Watthana": 0, "Bang Sue": 0, "Bang Na": 0, "Thung Khru": 0, "Phaya Thai": 0, "Vadhana": 0,
    "Ratchathewi": 0, "Bangkok Yai": 0, "Bang Khun Thian": 0, "Bang Khae": 0, "Dusit": 0, "Phra Nakhon": 0,
    "Bang Kho Laem": 0, "Yan Nawa": 0, "Bangkok Noi": 0, "Khlong San": 0, "Thon Buri": 0, "Bang Rak": 0, "Pathum Wan": 0,
    "Pom Prap Sattru Phai": 0, "Samphanthawong": 0, "Sathon": 0, "Khlong Toei": 0, "Phasi Charoen": 0, "Nong Khaem": 0,
    "Rat Burana": 0, "Chom Thong": 0,
}

# Saturday 3 Oct, morning to ~08:05. On 2 Oct local afternoon storms: 58 mm at BMA Bang Bon, 20.6 mm at TMD Bang Na,
# ~10 mm Bang Kapi and Bang Khae; no new street flooding reported overnight. Floodboard (08:04): roads with water 47 km
# (103 km a day earlier), 9 km impassable, BMA sensors 3 of 236 wet. Disaster declaration unchanged (29 districts).
# Citizen (Traffy) reports are unverified. Levels start from the state carried over from 2 Oct (carry.json).
OBS_03 = {
    "Lat Krabang": 3,      # Kheha Romklao -30-50 cm (BMA) or -20 cm (PPTV), chest-deep spots; sois 60-85 cm; Chao Khun Thahan knee-deep
    "Nong Chok": 3,        # Royal Park Ville knee-deep inside homes, Flora Ville 45-80 cm, not falling; Floodboard "severe"
    "Min Buri": 3,         # Rat Uthit 58 ~80 cm, Ram 174 knee-deep, Nimit Mai ~45 cm; flat
    "Prawet": 3,           # Phatthanakan 65-69 knee to waist, R.9 Soi 87 ~40 cm (corrected from 2)
    "Saphan Sung": 2,      # BMA: villages improved; residents: Nakkila Laemthong 45-60 cm; Floodboard "improving"
    "Khlong Sam Wa": 2,    # Sena Villa ~40 cm, KC village knee-deep; small area
    "Bueng Kum": 2,        # Sahakorn village dyke nearly overtopped at 22:37, improved by 06:12; sois up to 45 cm (corrected from 0)
    "Sai Mai": 2,          # Or Ngoen communities need ~2 days; Phahonyothin by the Memorial 10-50 cm (corrected from 1)
    "Bang Kapi": 2,        # Khlong Chan dry; after 10.6 mm on 2 Oct some sois 10-45 cm, 0.8 km impassable (corrected from 3)
    "Suan Luang": 1,       # Srinakarin, On Nut up to 7 cm
    "Bang Khen": 1,        # spots up to 25 cm, improving
    "Wang Thonglang": 1,   # 0.8 km of road with water
    "Don Mueang": 1,       # Phahonyothin at Thupatemi still wet on 2 Oct
    "Lak Si": 1, "Khan Na Yao": 1,
    "Phra Khanong": 0, "Bang Bon": 0, "Chatuchak": 0, "Lat Phrao": 0, "Din Daeng": 0, "Huai Khwang": 0, "Bang Phlat": 0,
    "Taling Chan": 0, "Thawi Watthana": 0, "Bang Sue": 0, "Bang Na": 0, "Thung Khru": 0, "Phaya Thai": 0, "Vadhana": 0,
    "Ratchathewi": 0, "Bangkok Yai": 0, "Bang Khun Thian": 0, "Bang Khae": 0, "Dusit": 0, "Phra Nakhon": 0,
    "Bang Kho Laem": 0, "Yan Nawa": 0, "Bangkok Noi": 0, "Khlong San": 0, "Thon Buri": 0, "Bang Rak": 0, "Pathum Wan": 0,
    "Pom Prap Sattru Phai": 0, "Samphanthawong": 0, "Sathon": 0, "Khlong Toei": 0, "Phasi Charoen": 0, "Nong Khaem": 0,
    "Rat Burana": 0, "Chom Thong": 0,
}

# Friday 2 Oct, morning to ~07:50. On 1 Oct a 16-19 h storm with hail hit the north and west: 60 mm in Chatuchak,
# 42.6 mm in Taling Chan, 27 mm in Bang Khen (HII); the east stayed dry. High tides to 3 Oct slow the drainage. No
# change to the disaster declaration (29 districts). Floodboard (07:47): roads with water 103 km (226 km at 21:00),
# BMA sensors 6 of 236 wet, deepest 10 cm; "severe" Nong Chok, "significant" Lat Krabang, Saphan Sung, Min Buri,
# Khan Na Yao, Don Mueang. Citizen (Traffy) reports are unverified.
# Levels start from the state carried over from 1 Oct (carry.json) and follow the reports where they differ.
OBS_02 = {
    "Lat Krabang": 4,      # Lat Krabang Rd up to ~80 cm (1.2 km impassable), sois 30-45 cm; Kheha Romklao -20 cm on 1 Oct; BMA: ~a week
    "Nong Chok": 3,        # Flora Ville 60-90 cm, Royal Park Ville 60 cm, ground floors flooded; Floodboard "severe", area growing
    "Saphan Sung": 3,      # Kheha Thani 4 waist-deep, Rat Phatthana Rd 40-80 cm; stagnant
    "Prawet": 3,           # Phatthanakan 61 ~1 m (07:47), Kanchanaphisek 80 cm, On Nut 25 cm (Traffy)
    "Min Buri": 3,         # villages 45 cm (Ram 174, Seri Thai 70), Suwinthawong 25 cm and 2 km impassable; area flat
    "Bang Kapi": 3,        # Khlong Chan ~30 cm and drying (officials), but sois off Ramkhamhaeng 45-60 cm overnight (Traffy)
    "Sai Mai": 2,          # Vacharaphol and Phoem Sin 25 cm; Khlong Hok Wa 1 m below its bank (corrected from 3)
    "Khlong Sam Wa": 2,    # 30-50 cm in villages (Traffy), Floodboard "minor, improving"
    "Khan Na Yao": 2,      # Ram Inthra 93 65 cm, Seri Thai 59 60 cm (Traffy); Floodboard "significant"
    "Don Mueang": 2,       # Phahonyothin up to 80 cm, day 6 (Traffy); Floodboard "significant"
    "Chatuchak": 2,        # 60 mm on 1 Oct; Phahonyothin segment 45 cm (07:13), Soi Cement Thai 50 cm; main roads mostly dry
    "Lak Si": 2,           # storm water: Chaeng Watthana jammed on 1 Oct evening, spots 45 cm at 07:10; improving
    "Bueng Kum": 1,        # a single 50 cm report (Nawamin 81); carried state 22 mm
    "Suan Luang": 1,       # Phatthanakan and Srinakarin 7-10 cm (sensors)
    "Wang Thonglang": 1,   # Lat Phrao Rd 5 cm (sensor)
    "Lat Phrao": 1,        # Chok Chai 4 25 cm, a few villages (Traffy)
    "Phra Khanong": 1,     # Bang Chak: only clean-up reports since 1 Oct evening; Punnawithi 23 30 cm on 1 Oct 15:04
    "Huai Khwang": 1,      # Phetchaburi 30 cm on 1 Oct 22:18
    "Bang Phlat": 1,       # Charan Sanit Wong 44 30 cm on 1 Oct evening, receding
    "Taling Chan": 1,      # 42.6 mm on 1 Oct; Chimphli 15 cm (01:01)
    "Bang Khen": 1,        # 27 mm on 1 Oct; Floodboard max 10 cm
    "Thawi Watthana": 0, "Bang Sue": 0, "Bang Na": 0, "Thung Khru": 0, "Bang Bon": 0, "Din Daeng": 0,
    "Phaya Thai": 0, "Vadhana": 0, "Ratchathewi": 0, "Bangkok Yai": 0, "Bang Khun Thian": 0, "Bang Khae": 0,
    "Dusit": 0, "Phra Nakhon": 0, "Bang Kho Laem": 0, "Yan Nawa": 0, "Bangkok Noi": 0, "Khlong San": 0,
    "Thon Buri": 0, "Bang Rak": 0, "Pathum Wan": 0, "Pom Prap Sattru Phai": 0, "Samphanthawong": 0, "Sathon": 0,
    "Khlong Toei": 0, "Phasi Charoen": 0, "Nong Khaem": 0, "Rat Burana": 0, "Chom Thong": 0,
}

# Thursday 1 Oct, morning to ~07:40. Rain on 30 Sep only 14-16 h in the north (18.6 mm in Sai Mai), none overnight. No
# BMA list this morning; 29 districts keep the disaster declaration. Khlong Chan pumping since ~03:00 on 30 Sep (-50 cm),
# Kheha Romklao -10-12 cm, the Sai Mai dike on Khlong Hok Wa overtopped but held. Floodboard: roads with water 298 km
# (00:31) -> 107 km (07:12); BMA sensors 8 of 237 wet, none above 20 cm. Citizen (Traffy) reports are unverified.
# Levels start from the state carried over from 30 Sep (carry.json) and follow the reports where they differ.
OBS_01 = {
    "Lat Krabang": 4,      # Kheha Romklao zone 5 chest-deep, district office area 1-1.2 m; main-road sensors 5-10 cm
    "Bang Kapi": 3,        # Khlong Chan waist- to chest-deep at noon on 30 Sep, -50 cm since pumping; main roads dry
    "Saphan Sung": 3,      # Nakkila Laemthong waist-deep, homes flooded, day 5, stagnant (Thai PBS 20:55)
    "Prawet": 3,           # Traffy: Phatthanakan 61/65/74 50-120 cm, stagnant; Prawet Burirom canal slowest (+14 RID pumps)
    "Sai Mai": 3,          # Kheha Or Ngern high, Sai Mai Rd ~80 cm (Floodboard); 18.6 mm on 30 Sep
    "Nong Chok": 3,        # Flora Ville 45-50 cm, Suwinthawong 44 knee-deep (Traffy), stagnant
    "Khlong Sam Wa": 3,    # 25-50 cm (citizens), Hok Wa dike under watch
    "Min Buri": 3,         # Suwinthawong 15-30 cm, Hwy 304 impassable on 30 Sep; sensor 10 cm
    "Bueng Kum": 2,        # Seri Thai 57 50 cm, Sri Burapha closed (BMA list, 30 Sep 11:03)
    "Khan Na Yao": 2,      # Suan Siam Rd 30 cm (BMA list, 30 Sep); Traffy Seri Thai 59 ~70 cm
    "Don Mueang": 2,       # Phahonyothin near the Air Force memorial up to ~1 m after the rain on 30 Sep; Vibhavadi km 27-28
    "Wang Thonglang": 2,   # Traffy 30-45 cm in sois (05:06)
    "Phra Khanong": 2,     # Bang Chak sois (Sukhumvit 89/1, 93, Phueng Mi 1) 10-45 cm on 30 Sep, "not receding": canal backs up
    "Bang Khen": 1,        # Ram Inthra 5-20 cm, sensor 5 cm
    "Suan Luang": 1,       # sensors 5-15 cm
    "Lak Si": 1,           # ~20 cm at three spots, rest dry (district office 30 Sep)
    "Lat Phrao": 1,        # single spots (Traffy); 17.2 mm on the Sai Mai border on 30 Sep
    "Chatuchak": 0, "Thawi Watthana": 0, "Bang Phlat": 0, "Taling Chan": 0, "Huai Khwang": 0, "Bang Sue": 0,
    "Bang Na": 0, "Thung Khru": 0, "Bang Bon": 0, "Din Daeng": 0, "Phaya Thai": 0, "Vadhana": 0, "Ratchathewi": 0,
    "Bangkok Yai": 0, "Bang Khun Thian": 0, "Bang Khae": 0, "Dusit": 0, "Phra Nakhon": 0, "Bang Kho Laem": 0,
    "Yan Nawa": 0, "Bangkok Noi": 0, "Khlong San": 0, "Thon Buri": 0, "Bang Rak": 0, "Pathum Wan": 0,
    "Pom Prap Sattru Phai": 0, "Samphanthawong": 0, "Sathon": 0, "Khlong Toei": 0, "Phasi Charoen": 0,
    "Nong Khaem": 0, "Rat Burana": 0, "Chom Thong": 0,
}

# Wednesday 30 Sep, morning to ~07:40. A dry day: 24 h to 07:00 at most 6 mm (Wat Bang Bua), 0 mm elsewhere. BMA
# (19:54 on 29 Sep) ended the disaster declaration in 21 districts; 29 remain (15 "high impact" with schools closed
# to 2 Oct, 14 "moderate"). DDPM Cell Broadcast (18:45): Khlong Hok Wa Sai Lang on the Pathum Thani border may
# overtop into Sai Mai, Khlong Sam Wa and Nong Chok (29 Sep - 4 Oct). BMA: main roads in Kaset, Bang Bua,
# Ramkhamhaeng, Hua Mak and Phatthanakan in 1-2 days, the east 5-7 days, communities about 7 days. Levels start
# from the state carried over from 29 Sep (carry.json) and follow the reports where they differ.
OBS_30 = {
    "Bang Kapi": 4,        # Khlong Chan flats 1-1.5 m, Happy Land waist-deep; Saen Saep "dropped a lot" (governor)
    "Lat Krabang": 4,      # Kheha Romklao 1-1.5 m, day 5, "not receding"; >500 cars under water
    "Nong Chok": 3, "Khlong Sam Wa": 3,              # Hok Wa canal overtopping alert; Traffy up to 50-100 cm
    "Sai Mai": 3,          # Khlong Thanon housing 30-80 cm; Phoem Sin and Watcharaphon flooded at 22:00
    "Saphan Sung": 3,      # Nakkila Laemthong village waist- to chest-deep, -5 cm a day
    "Min Buri": 3,         # Suwinthawong 20-30+ cm, communities deeper; BMA: east roads 5-7 days
    "Bang Khen": 2,        # Kheha Ram Inthra 25-30 cm; Lat Phrao canal at Wat Bang Bua down 21 cm, still over the bank
    "Prawet": 2,           # Prawet Burirom canal the slowest to drain; roads 5-7 days; Traffy 50-80 cm in sois
    "Bueng Kum": 2,        # Moo Ban Sahakorn (~2,000 homes) down ~20 cm; Nawamin 38 20 cm
    "Suan Luang": 2,       # Phatthanakan at Srinakarin 24.7 cm at 13:19 on 29 Sep, falling
    "Lak Si": 1,           # Chaeng Watthana Soi 10 at kerb level, pumps running
    "Khan Na Yao": 1,      # no official data; Traffy ~45 cm in villages
    "Wang Thonglang": 1,   # Lat Phrao 122 15.5 cm at 13:19 on 29 Sep (30 in the morning)
    "Chatuchak": 1,        # Phahonyothin Kaset - Soi 49/1 15-20 cm, passable (21:45 on 29 Sep)
    "Don Mueang": 1,       # "moderate"; the deep water on Phahonyothin is at Lam Luk Ka (Pathum Thani side)
    "Phra Khanong": 1,     # "moderate"; BMA: water rising from the drains is temporary backflow
    "Thawi Watthana": 1,   # "moderate"; Maha Sawat canal over its bank in Taling Chan at 21:00 on 29 Sep
    "Bang Phlat": 0, "Din Daeng": 0, "Dusit": 0, "Thung Khru": 0, "Bang Sue": 0, "Bang Na": 0, "Bang Bon": 0,
    "Phaya Thai": 0, "Ratchathewi": 0, "Vadhana": 0, "Huai Khwang": 0,   # "moderate", ~0 km of wet roads
    # disaster declaration ended on 29 Sep
    "Lat Phrao": 0, "Phra Nakhon": 0, "Bang Rak": 0, "Pathum Wan": 0, "Pom Prap Sattru Phai": 0,
    "Samphanthawong": 0, "Yan Nawa": 0, "Sathon": 0, "Bang Kho Laem": 0, "Khlong Toei": 0, "Khlong San": 0,
    "Thon Buri": 0, "Bangkok Yai": 0, "Bangkok Noi": 0, "Taling Chan": 0, "Bang Khun Thian": 0, "Phasi Charoen": 0,
    "Nong Khaem": 0, "Rat Burana": 0, "Chom Thong": 0, "Bang Khae": 0,
}

# Tuesday 29 Sep, morning to ~07:40. Rain on 28 Sep fell mostly 09-13 h (HII 24 h to 07:00: Sai Mai 17.4 mm, Bang Kapi
# and Lat Phrao 16.8, Lat Krabang 6.6); the night was dry. BMA at 05:30: standing water in 8 districts (Lat Krabang,
# Bang Kapi, Min Buri, Saphan Sung, Suan Luang, Bueng Kum, Khlong Sam Wa, Sai Mai), 23 roads to avoid, Phatthanakan,
# Ramkhamhaeng and Lat Krabang roads receding; northern water starting to raise levels in Bang Phlat and Thawi
# Watthana. Road sensors 07:30 via Floodboard. Levels start from the state carried over from 28 Sep (carry.json)
# and follow the reports where they differ.
OBS_29 = {
    "Bang Kapi": 4,        # Khlong Chan flats 1-1.5 m, chest-deep on the evening of 28 Sep; pumping in 1-2 days if dry
    "Lat Krabang": 4,      # Kheha Romklao >1 m, "dropping slowly" (governor, 21:45 28 Sep); Chao Khun Thahan 5-10 cm
    "Min Buri": 3, "Khlong Sam Wa": 3, "Nong Chok": 3,   # villages 30-60 cm and more, steady (Traffy reports)
    "Sai Mai": 3,          # main roads 10-15 cm and falling, villages 30-60 cm (Traffy)
    "Saphan Sung": 3,      # on the BMA list; villages off Ramkhamhaeng 112/118 ~45 cm (Traffy); was 2 on 28 Sep
    "Bang Khen": 3,        # Lat Phrao canal at Wat Bang Bua 0.37 m over the bank; Phahonyothin 5 cm; communities 20-40 cm
    "Suan Luang": 2,       # Phatthanakan at Srinakarin 29.5 cm (43.6 the day before)
    "Bueng Kum": 2,        # Nawamin 46 24 cm (37)
    "Wang Thonglang": 2,   # Lat Phrao 122 30 cm (44)
    "Prawet": 2, "Khan Na Yao": 2,                   # On Nut, Chaloem Phrakiat R9 and Seri Thai on the avoid list
    "Lak Si": 2,           # Chaeng Watthana on the avoid list; Prem Prachakorn canal 0.45 m over the bank upstream
    "Lat Phrao": 1,        # Sukhonthasawat 0 cm (20+ on 28 Sep); Lat Phrao - Wang Hin minor water
    "Don Mueang": 1,       # Chang Akat Uthit 5-10 cm; Vibhavadi outbound on the avoid list
    "Chatuchak": 1,        # Phahonyothin at Kasetsart 10 cm (20+ on 28 Sep)
    "Huai Khwang": 1,
    "Phra Khanong": 1,     # Wachirathammasathit (Sukhumvit 101/1) on the avoid list
    "Thawi Watthana": 1, "Bang Phlat": 1,           # BMA: northern water starting to raise levels
    "Bang Khun Thian": 1,  # tidal; ONWR high-tide watch 29 Sep - 4 Oct (Rama 2)
    "Bang Na": 0, "Vadhana": 0, "Khlong Toei": 0, "Yan Nawa": 0, "Bang Kho Laem": 0, "Din Daeng": 0,
    "Phaya Thai": 0, "Bang Sue": 0, "Ratchathewi": 0, "Dusit": 0, "Pathum Wan": 0, "Bang Rak": 0, "Sathon": 0,
    "Phra Nakhon": 0, "Samphanthawong": 0, "Pom Prap Sattru Phai": 0, "Taling Chan": 0, "Bang Khae": 0,
    "Nong Khaem": 0, "Phasi Charoen": 0, "Chom Thong": 0, "Bangkok Yai": 0, "Bangkok Noi": 0, "Thon Buri": 0,
    "Khlong San": 0, "Rat Burana": 0, "Thung Khru": 0, "Bang Bon": 0,
}

# Monday 28 Sep, morning to ~09:30. A thunderstorm over Suvarnabhumi at 01-04 h: in the 24 h to 07:00 up to 63 mm
# at the Saen Saep sluice (Nong Chok), 46.5 mm overnight in Lat Krabang, TMD Suvarnabhumi 48.8 mm. BMA (evening
# 27 Sep): 44 flooded road points on 29 roads. Khlong Chan ~1.5 m, Kheha Romklao >1 m. BMA expects Sai Mai, Khlong
# Chan, Kheha Romklao and Khu Bon to start receding today and all areas back to normal by 1 Oct (Kheha Romklao
# ~7 days). Levels start from the state carried over from 27 Sep (carry.json) and follow the reports where they differ.
OBS_28 = {
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
