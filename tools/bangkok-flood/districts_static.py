# Static knowledge-based parameters for Bangkok's 50 districts.
# zone: core | mid | outer | east | coast
# low: relative lowness / subsidence 0..1 (expert estimate, blended with DEM later)
# D0: effective drainage of standing water, mm/day (pumps, tunnels, canal capacity)
# rc: base runoff coefficient (share of rain that becomes surface water)
# riv: exposure of riverfront strips outside the Chao Phraya flood wall 0..1
# tide: dependence of drainage on sea tide (outflow to river mouth / Gulf) 0..1
# ext: exposure to runoff arriving from neighbouring provinces (north/east/west fields) 0..1
# ru: Russian name; poi: what a traveller knows there

D = {
 "Phra Nakhon":        dict(ru="Пхранакхон", zone="core", low=0.30, D0=90, rc=0.85, riv=0.6, tide=0.15, ext=0.0, poi="Большой дворец, Ват Пхо, Каосан"),
 "Pom Prap Sattru Phai": dict(ru="Помпрап", zone="core", low=0.35, D0=90, rc=0.88, riv=0.2, tide=0.15, ext=0.0, poi="Золотая гора, Ворачак"),
 "Samphanthawong":     dict(ru="Сампхантхавонг", zone="core", low=0.35, D0=85, rc=0.9, riv=0.6, tide=0.2, ext=0.0, poi="Чайнатаун, Яоварат"),
 "Bang Rak":           dict(ru="Банграк", zone="core", low=0.40, D0=85, rc=0.9, riv=0.4, tide=0.2, ext=0.0, poi="Силом, Патпонг, отели на реке"),
 "Pathum Wan":         dict(ru="Патхумван", zone="core", low=0.40, D0=85, rc=0.88, riv=0.0, tide=0.1, ext=0.0, poi="Сиам, Ратчапрасонг, парк Лумпини"),
 "Sathon":             dict(ru="Сатхон", zone="core", low=0.42, D0=80, rc=0.88, riv=0.3, tide=0.2, ext=0.0, poi="Сатхон, Сурасак, Чонг Нонси"),
 "Ratchathewi":        dict(ru="Ратчатхеви", zone="core", low=0.42, D0=75, rc=0.9, riv=0.0, tide=0.1, ext=0.0, poi="Пратунам, Байок, Монумент Победы"),
 "Phaya Thai":         dict(ru="Пхаятхай", zone="core", low=0.40, D0=75, rc=0.88, riv=0.0, tide=0.1, ext=0.0, poi="Ари, Саналуанг, Монумент Победы"),
 "Dusit":              dict(ru="Дусит", zone="core", low=0.35, D0=80, rc=0.8, riv=0.5, tide=0.15, ext=0.0, poi="Дворец Дусит, пирс Тхевет"),
 "Khlong San":         dict(ru="Кхлонгсан", zone="core", low=0.45, D0=70, rc=0.85, riv=0.6, tide=0.25, ext=0.0, poi="ICONSIAM, отели на западном берегу"),
 "Thon Buri":          dict(ru="Тхонбури", zone="core", low=0.45, D0=70, rc=0.85, riv=0.5, tide=0.25, ext=0.0, poi="Вонгвиан Яй"),
 "Bangkok Yai":        dict(ru="Бангкок-Яй", zone="core", low=0.42, D0=70, rc=0.82, riv=0.5, tide=0.2, ext=0.0, poi="Ват Арун"),
 "Bangkok Noi":        dict(ru="Бангкок-Ной", zone="core", low=0.45, D0=65, rc=0.82, riv=0.7, tide=0.2, ext=0.0, poi="госпиталь Сирирадж, вокзал Тхонбури"),
 "Vadhana":            dict(ru="Ваттхана", zone="mid", low=0.55, D0=65, rc=0.9, riv=0.0, tide=0.2, ext=0.0, poi="Сукхумвит: Нана, Асок, Пхромпхонг, Тхонглор, Экамай"),
 "Khlong Toei":        dict(ru="Кхлонгтой", zone="mid", low=0.55, D0=65, rc=0.88, riv=0.4, tide=0.35, ext=0.0, poi="Сукхумвит 1–24, парк Бенчакитти, порт"),
 "Huai Khwang":        dict(ru="Хуайкхванг", zone="mid", low=0.50, D0=60, rc=0.88, riv=0.0, tide=0.15, ext=0.0, poi="Ратчада, Рама IX, Jodd Fairs"),
 "Din Daeng":          dict(ru="Диндэнг", zone="mid", low=0.52, D0=60, rc=0.9, riv=0.0, tide=0.15, ext=0.0, poi="Вибхавади, Прачасонгкхро"),
 "Chatuchak":          dict(ru="Чатучак", zone="mid", low=0.55, D0=55, rc=0.85, riv=0.0, tide=0.15, ext=0.05, poi="рынок Чатучак, Мо Чит, Ладпрао"),
 "Bang Sue":           dict(ru="Бангсы", zone="mid", low=0.45, D0=65, rc=0.85, riv=0.4, tide=0.15, ext=0.0, poi="вокзал Крунгтхеп Апхиват"),
 "Bang Phlat":         dict(ru="Бангпхлат", zone="mid", low=0.50, D0=60, rc=0.82, riv=0.9, tide=0.2, ext=0.0, poi="Пинклао, Бангъикхан (набережная)"),
 "Yan Nawa":           dict(ru="Яннава", zone="mid", low=0.50, D0=65, rc=0.85, riv=0.5, tide=0.45, ext=0.0, poi="Рама III, Чан"),
 "Bang Kho Laem":      dict(ru="Бангкхолэм", zone="mid", low=0.50, D0=60, rc=0.85, riv=0.6, tide=0.45, ext=0.0, poi="Asiatique, Чароенкрунг-юг"),
 "Rat Burana":         dict(ru="Ратбурана", zone="mid", low=0.58, D0=55, rc=0.8, riv=0.6, tide=0.55, ext=0.0, poi="Сук Сават"),
 "Wang Thonglang":     dict(ru="Вангтхонланг", zone="mid", low=0.55, D0=55, rc=0.85, riv=0.0, tide=0.15, ext=0.0, poi="Чок Чай 4, Праду"),
 "Lat Phrao":          dict(ru="Латпхрао", zone="mid", low=0.60, D0=48, rc=0.82, riv=0.0, tide=0.15, ext=0.05, poi="Латпхрао, Сена Никхом"),
 "Phra Khanong":       dict(ru="Пхраканонг", zone="mid", low=0.60, D0=55, rc=0.85, riv=0.2, tide=0.4, ext=0.0, poi="Он Нут, Сукхумвит 71–101"),
 "Chom Thong":         dict(ru="Чомтхонг", zone="mid", low=0.58, D0=48, rc=0.8, riv=0.1, tide=0.35, ext=0.0, poi="Эккачай, Рама II"),
 "Phasi Charoen":      dict(ru="Пхасичароен", zone="mid", low=0.56, D0=48, rc=0.8, riv=0.0, tide=0.2, ext=0.05, poi="Пхеткасем, The Mall Bangkhae"),
 "Bang Kapi":          dict(ru="Бангкапи", zone="outer", low=0.62, D0=42, rc=0.8, riv=0.0, tide=0.2, ext=0.05, poi="Рамкхамхэнг, The Mall Bangkapi"),
 "Bueng Kum":          dict(ru="Бынгкум", zone="outer", low=0.64, D0=40, rc=0.75, riv=0.0, tide=0.2, ext=0.15, poi="Навамин, Сериттхай"),
 "Khan Na Yao":        dict(ru="Кханнаяо", zone="outer", low=0.66, D0=36, rc=0.72, riv=0.0, tide=0.2, ext=0.3, poi="Рам Интхра, Fashion Island"),
 "Saphan Sung":        dict(ru="Сапхансунг", zone="outer", low=0.72, D0=32, rc=0.72, riv=0.0, tide=0.25, ext=0.25, poi="Рамкхамхэнг (дальний)"),
 "Suan Luang":         dict(ru="Суанлуанг", zone="outer", low=0.68, D0=38, rc=0.78, riv=0.0, tide=0.3, ext=0.05, poi="Паттанакан, Сринакарин"),
 "Prawet":             dict(ru="Правет", zone="outer", low=0.74, D0=32, rc=0.75, riv=0.0, tide=0.35, ext=0.2, poi="парк Рама IX, Сринакарин"),
 "Bang Na":            dict(ru="Бангна", zone="outer", low=0.68, D0=40, rc=0.8, riv=0.2, tide=0.45, ext=0.0, poi="Бангна-Трат, BITEC"),
 "Bang Khen":          dict(ru="Бангкхен", zone="outer", low=0.58, D0=45, rc=0.78, riv=0.0, tide=0.1, ext=0.45, poi="Рам Интхра, Пхахонйотхин"),
 "Lak Si":             dict(ru="Лаксы", zone="outer", low=0.56, D0=45, rc=0.8, riv=0.0, tide=0.1, ext=0.45, poi="Чэнгваттхана, Госкомплекс"),
 "Don Mueang":         dict(ru="Донмыанг", zone="outer", low=0.56, D0=42, rc=0.78, riv=0.0, tide=0.1, ext=0.6, poi="аэропорт Донмыанг (DMK)"),
 "Sai Mai":            dict(ru="Саймай", zone="outer", low=0.70, D0=30, rc=0.7, riv=0.0, tide=0.1, ext=0.75, poi="Пхахонйотхин (север)"),
 "Bang Khae":          dict(ru="Бангкхэ", zone="outer", low=0.62, D0=40, rc=0.75, riv=0.0, tide=0.2, ext=0.3, poi="Пхеткасем, Сиам Каннал"),
 "Nong Khaem":         dict(ru="Нонгкхэм", zone="outer", low=0.66, D0=34, rc=0.7, riv=0.0, tide=0.25, ext=0.4, poi="Пхеткасем (запад)"),
 "Taling Chan":        dict(ru="Талингчан", zone="outer", low=0.66, D0=34, rc=0.65, riv=0.1, tide=0.2, ext=0.3, poi="плавучий рынок Талингчан"),
 "Thawi Watthana":     dict(ru="Тхавиваттхана", zone="outer", low=0.70, D0=30, rc=0.62, riv=0.0, tide=0.2, ext=0.5, poi="Пхуттхамонтхон Сай"),
 "Bang Bon":           dict(ru="Бангбон", zone="outer", low=0.78, D0=30, rc=0.7, riv=0.0, tide=0.45, ext=0.3, poi="Эккачай (юг)"),
 "Thung Khru":         dict(ru="Тхунгкхру", zone="outer", low=0.74, D0=34, rc=0.72, riv=0.4, tide=0.6, ext=0.0, poi="Прача Утхит"),
 "Lat Krabang":        dict(ru="Латкрабанг", zone="east", low=0.86, D0=28, rc=0.65, riv=0.0, tide=0.35, ext=0.5, poi="рядом аэропорт Суварнабхуми (BKK)"),
 "Min Buri":           dict(ru="Минбури", zone="east", low=0.82, D0=28, rc=0.68, riv=0.0, tide=0.25, ext=0.6, poi="рынок Минбури, Сери Тхай"),
 "Nong Chok":          dict(ru="Нонгчок", zone="east", low=0.90, D0=22, rc=0.55, riv=0.0, tide=0.3, ext=1.0, poi="сельские районы, польдеры"),
 "Khlong Sam Wa":      dict(ru="Кхлонгсамва", zone="east", low=0.86, D0=25, rc=0.6, riv=0.0, tide=0.2, ext=0.9, poi="Сафари Ворлд"),
 "Bang Khun Thian":    dict(ru="Бангкхунтхиан", zone="coast", low=0.95, D0=22, rc=0.62, riv=0.1, tide=1.0, ext=0.2, poi="побережье, мангры"),
}
