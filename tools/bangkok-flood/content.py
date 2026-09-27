# Page content (Russian). Facts compiled from BMA/DDPM/TMD reports in Thai and English media, 24-26 Sep 2026.
from districts_static import D

LEVELS = [
    dict(name="Сухо", short="сухо", depth="0 см",
         desc="Обычный день сезона дождей: после ливня вода уходит за час-два."),
    dict(name="Лужи на низких улицах", short="лужи", depth="до 10 см",
         desc="После ливня вода стоит у бордюров и в сои, уходит за несколько часов. Пройти можно."),
    dict(name="Улицы в воде", short="улицы в воде", depth="10–30 см",
         desc="Часть дорог непроезжа для легковых, пробки, такси и Grab отказываются ехать. BTS и MRT работают."),
    dict(name="Вода во дворах и домах", short="дома в воде", depth="30–60 см",
         desc="Затоплены сои, дворы и первые этажи у каналов, вода держится днями. Туда лучше не ехать."),
    dict(name="Бедствие", short="бедствие", depth="60+ см",
         desc="Вода по пояс и выше, эвакуация, лодки. Держись подальше."),
]

E = "2026-09-25"  # start of the event: notes are hidden on earlier days

# notes per district: kind 'obs' (red dot) or 'info' (blue dot); shown from 'frm' to 'until'
NOTES = {
    "Bang Kapi": [
        dict(frm="2026-09-27", text="27.09: в жилом комплексе Кхлонг Чан всё ещё около 1 м, местами по пояс; жители укрываются на скайуоке. Перед рассветом снова шёл дождь.", until="2026-10-06"),
        dict(frm=E, text="26.09: в Кхлонг Чан вода по грудь, машины под водой; погибла женщина от удара током.", until="2026-09-26"),
        dict(frm=E, text="Канал Саенсэп выходил из берегов у перекрёстка Бангкапи; на Рамкхамхэнг напротив сои 43 — 25–30 см (27.09).", until="2026-09-29"),
    ],
    "Lat Krabang": [
        dict(frm="2026-09-27", text="27.09: в общине Кхеха Ромклао вода от колена до груди, местами по плечи; нет света и воды с вечера 26.09. Работает армия (лодки, грузовики, полевая кухня), пункты размещения — школа Кхеха Ромклао и KMITL.", until="2026-10-08"),
        dict(frm=E, text="Lat Krabang Rd у Кинг Кэо — 15–20 см, непроезжа (25–26.09); Chao Khun Thahan Rd — 20+ см (27.09).", until="2026-09-30"),
        dict(kind="info", text="Аэропорт Суварнабхуми (провинция Самутпракан) за кольцевой дамбой и работает. TAT советует ехать не через Латкрабанг, а по трассе M7 или Бурапха Витхи."),
    ],
    "Min Buri": [
        dict(frm=E, text="Максимум осадков за событие: 274,5 мм за 48 часов.", until="2026-10-05"),
        dict(frm="2026-09-27", text="27.09: в общинах вода всё ещё высокая; один из трёх районов, куда в первую очередь идёт помощь.", until="2026-10-04"),
    ],
    "Khlong Sam Wa": [
        dict(frm=E, text="273 мм за 48 часов, 168,5 мм только за 25.09.", until="2026-10-05"),
        dict(frm="2026-09-26", text="По неподтверждённым данным — 0,3–0,7 м в трёх подрайонах. Из Патхумтхани продолжает поступать вода.", until="2026-10-05"),
    ],
    "Nong Chok": [
        dict(frm=E, text="25.09 объявлен зоной бедствия (все 8 подрайонов).", until="2026-10-08"),
        dict(frm="2026-09-27", text="27.09: 83 мм за ночь у шлюза Саенсэп; по неподтверждённым данным, в воде 80 общин и 15 дорог (10–40 см).", until="2026-10-06"),
    ],
    "Khan Na Yao": [dict(frm=E, text="25.09 объявлен зоной бедствия; Ram Inthra Rd — 20–28 см.", until="2026-09-30")],
    "Suan Luang": [
        dict(frm=E, text="25.09 объявлен зоной бедствия; в сои Он Нута вода по колено.", until="2026-09-30"),
        dict(frm="2026-09-27", text="27.09: перекрёсток Пхетчабури — Паттанакан непроезжий, канал Правет на «красном» уровне.", until="2026-10-01"),
    ],
    "Prawet": [dict(frm=E, text="Канал Правет-Буриром на «красном» уровне; сои Он Нута в воде (27.09).", until="2026-10-01")],
    "Bueng Kum": [
        dict(frm=E, text="26.09: двое утонувших (73 и 78 лет) — по данным Википедии, в Бынгкуме.", until="2026-09-28"),
        dict(frm="2026-09-27", text="27.09: Nawamin — 20+ см у сои 38–59, 107 и 155.", until="2026-09-30"),
    ],
    "Wang Thonglang": [dict(frm=E, text="205,5 мм за сутки к 26.09. 27.09: Lat Phrao 122 — 20–25 см, Lat Phrao Rd от Big C к Бангкапи непроезжа.", until="2026-09-29")],
    "Saphan Sung": [dict(frm=E, text="203,5 мм за сутки к 26.09; Рамкхамхэнг в «красной» зоне.", until="2026-09-29")],
    "Chatuchak": [
        dict(frm=E, text="210 мм за сутки к утру 26.09 — максимум по городу; Вибхавади — 30 см, у обочины до 1 м.", until="2026-09-28"),
        dict(frm="2026-09-27", text="27.09: Phahonyothin у университета Шрипатум ещё в воде; Вибхавади на выезд — 20+ см у развязки Вибхавади — Рангсит.", until="2026-09-29"),
    ],
    "Bang Khen": [
        dict(frm=E, text="Банг Буа (Phahonyothin 49/1): 26.09 около 60 см, местами больше 1 м.", until="2026-09-29"),
        dict(frm="2026-09-27", text="27.09: полиция — вода на всех точках: Phahonyothin, Prasert-Manukitch, Ngamwongwan, Ram Inthra; легковым не проехать.", until="2026-09-30"),
    ],
    "Lak Si": [dict(frm=E, text="26.09 Chaeng Watthana — около 50 см, закрыта; 27.09 у NT снова проезжа, у BTS Lak Si ещё вода. Канал Премпрачакон на «красном» уровне.", until="2026-09-29")],
    "Don Mueang": [
        dict(frm="2026-09-27", text="27.09: 71 мм за ночь; канал Премпрачакон на «красном» уровне. 26.09 подтопило рулёжную дорожку аэропорта, рейсы не пострадали.", until="2026-09-30"),
        dict(kind="info", text="Аэропорт Донмыанг работает. TAT советует ехать по Don Muang Tollway; такси по счётчику 27.09 временно не работали."),
    ],
    "Sai Mai": [dict(frm="2026-09-27", text="27.09: 85 мм за ночь — максимум по городу; перекрёсток Сапхан Май (Big C) в воде, канал Хок Ва на пределе.", until="2026-10-01")],
    "Lat Phrao": [dict(frm=E, text="Lat Phrao Rd в «красной» зоне: канал Саенсэп выходит на дорогу.", until="2026-09-29")],
    "Bang Sue": [dict(kind="info", frm=E, text="26.09 открыты 2 пункта временного размещения; отдельных сообщений о подтоплениях не было.", until="2026-09-29")],
    "Vadhana": [
        dict(frm=E, text="26.09: Сукхумвит 63 (Экамай) непроезжа, на перекрёстке Экамай-Север заглохшие машины.", until="2026-09-26"),
        dict(frm="2026-09-27", kind="info", text="27.09: Экамай высыхает, воду откачивают в канал Кхлонг Тэй.", until="2026-09-29"),
    ],
    "Khlong Toei": [dict(kind="info", frm=E, text="27.09: Сукхумвит 26 снова в норме.", until="2026-09-29")],
    "Phra Khanong": [dict(frm=E, text="Сукхумвит 71 и 101/1 в воде (27.09); насосная станция Пхраканонг (145 м³/с) на пределе.", until="2026-09-30")],
    "Bang Na": [dict(frm=E, text="Съезд Bang Na–Trat в воде (25–27.09).", until="2026-09-29")],
    "Huai Khwang": [dict(frm=E, text="201 мм за сутки к 26.09; Ratchadaphisek и Rama 9 — «красные» 26.09.", until="2026-09-28")],
    "Ratchathewi": [dict(frm="2026-09-27", text="27.09: Пхетчабури у перекрёстка Асок (у железной дороги) — 30–40 см.", until="2026-09-28")],
    "Din Daeng": [dict(frm=E, text="26.09: Din Daeng Rd и Asok — Din Daeng в «красной» зоне.", until="2026-09-27")],
    "Phaya Thai": [dict(frm=E, text="203 мм за сутки к 26.09; подтоплены улицы в Ари.", until="2026-09-27")],
    "Thawi Watthana": [dict(frm="2026-09-26", text="26.09 был в списке районов с серьёзным подтоплением (от 25 см или непроезжие улицы).", until="2026-09-28")],
    "Bang Khun Thian": [dict(frm=E, text="Rama II у Lotus — «оранжевая» 26.09, напротив сои 10 — около 5 см.", until="2026-09-28")],
    "Bang Bon": [dict(frm=E, text="Ekkachai Rd у Ват Кампхэнг — «оранжевая» 26.09.", until="2026-09-27")],
}
for n in ["Pathum Wan", "Bang Rak", "Sathon", "Phra Nakhon", "Samphanthawong", "Pom Prap Sattru Phai"]:
    NOTES.setdefault(n, []).append(dict(kind="info", frm=E, text="25–27.09 точек подтопления в центре не было: он дренируется быстрее всего.", until="2026-09-30"))
for n in ["Taling Chan", "Bang Khae", "Nong Khaem", "Phasi Charoen", "Chom Thong", "Bangkok Yai", "Bang Phlat", "Thon Buri",
          "Rat Burana", "Thung Khru"]:
    NOTES.setdefault(n, []).append(dict(kind="info", frm=E, text="Западный берег 26–27.09: лишь лужи до 5 см, вода быстро уходит.", until="2026-09-30"))
for n in ["Dusit", "Phra Nakhon", "Bang Kho Laem", "Yan Nawa", "Bangkok Noi", "Khlong San"]:
    NOTES.setdefault(n, []).append(dict(kind="info", text="Здесь есть общины за пределами речной дамбы (всего 11 общин, ~320 домов в 6 районах): их подтапливает в сильный прилив."))

HOTSPOTS = [
    dict(name="Сукхумвит 63 (Экамай)", lat=13.7390, lon=100.5890, note="непроезжа 26.09, к 27.09 высыхает", frm="2026-09-25", to="2026-09-26"),
    dict(name="Вибхавади (Чатучак)", lat=13.8288, lon=100.5600, note="30 см, у обочины до 1 м (26.09); 20+ см (27.09)", frm="2026-09-25", to="2026-09-27"),
    dict(name="Рамкхамхэнг у университета", lat=13.7562, lon=100.6174, note="непроезжа 26.09; 25–30 см у сои 43 (27.09)", frm="2026-09-25", to="2026-09-27"),
    dict(name="Lat Krabang Rd / Кинг Кэо", lat=13.7215, lon=100.7400, note="15–20 см на 800 м, непроезжа", frm="2026-09-25", to="2026-09-27"),
    dict(name="Сена Никхом", lat=13.8354, lon=100.5780, note="непроезжа для легковых, 26.09", frm="2026-09-25", to="2026-09-26"),
    dict(name="Чэнгваттхана у Госкомплекса", lat=13.8880, lon=100.5720, note="около 50 см 26.09, к 27.09 проезжа", frm="2026-09-25", to="2026-09-26"),
    dict(name="Жилой комплекс Кхлонг Чан", lat=13.7722, lon=100.6529, note="около 1 м, местами по пояс (27.09)", frm="2026-09-25", to="2026-09-27"),
    dict(name="Банг Буа (Phahonyothin 49/1)", lat=13.8500, lon=100.5850, note="около 60 см, местами >1 м (26.09)", frm="2026-09-25", to="2026-09-27"),
    dict(name="Кхеха Ромклао (Латкрабанг)", lat=13.7630, lon=100.7250, note="от колена до плеч, нет света (27.09)", frm="2026-09-26", to="2026-09-27"),
    dict(name="Перекрёсток Сапхан Май", lat=13.8905, lon=100.6056, note="глубокая вода, 27.09", frm="2026-09-27", to="2026-09-27"),
    dict(name="Пхетчабури у Асока", lat=13.7489, lon=100.5634, note="30–40 см, 27.09", frm="2026-09-27", to="2026-09-27"),
    dict(name="Phahonyothin у Шрипатум", lat=13.8548, lon=100.5855, note="ещё в воде, 27.09", frm="2026-09-27", to="2026-09-27"),
]

POIS = [
    dict(name="BKK", lat=13.6900, lon=100.7501, air=True),
    dict(name="DMK", lat=13.9126, lon=100.6067, air=True),
    dict(name="Большой дворец", lat=13.7500, lon=100.4913),
    dict(name="Каосан", lat=13.7589, lon=100.4974),
    dict(name="Сиам", lat=13.7456, lon=100.5341),
    dict(name="Пратунам", lat=13.7510, lon=100.5406),
    dict(name="Асок", lat=13.7373, lon=100.5603),
    dict(name="Тхонглор", lat=13.7243, lon=100.5784),
    dict(name="Экамай", lat=13.7196, lon=100.5853),
    dict(name="Силом", lat=13.7286, lon=100.5341),
    dict(name="Чайнатаун", lat=13.7400, lon=100.5100),
    dict(name="ICONSIAM", lat=13.7266, lon=100.5103),
    dict(name="Asiatique", lat=13.7045, lon=100.5030),
    dict(name="Рынок Чатучак", lat=13.7999, lon=100.5505),
    dict(name="Ари", lat=13.7797, lon=100.5446),
    dict(name="Он Нут", lat=13.7057, lon=100.6011),
]

PROVINCES = [
    dict(name="Нонтхабури", lat=13.885, lon=100.43),
    dict(name="Патхумтхани", lat=13.966, lon=100.72),
    dict(name="Самутпракан", lat=13.585, lon=100.70),
    dict(name="Самутсакхон", lat=13.535, lon=100.34),
    dict(name="Чачоэнгсао", lat=13.70, lon=100.925),
]

SPOTS = [
    dict(name="Сукхумвит: Асок — Тхонглор — Экамай", d="Vadhana"),
    dict(name="Сукхумвит 1–24, Нана", d="Khlong Toei"),
    dict(name="Сиам, Ратчапрасонг, Лумпини", d="Pathum Wan"),
    dict(name="Пратунам, Монумент Победы", d="Ratchathewi"),
    dict(name="Силом, Патпонг", d="Bang Rak"),
    dict(name="Сатхон", d="Sathon"),
    dict(name="Каосан, Большой дворец", d="Phra Nakhon"),
    dict(name="Чайнатаун (Яоварат)", d="Samphanthawong"),
    dict(name="ICONSIAM, западный берег", d="Khlong San"),
    dict(name="Ари", d="Phaya Thai"),
    dict(name="Рынок Чатучак", d="Chatuchak"),
    dict(name="Ратчада, Рама IX", d="Huai Khwang"),
    dict(name="Он Нут", d="Phra Khanong"),
    dict(name="Латкрабанг, у аэропорта BKK", d="Lat Krabang"),
    dict(name="Донмыанг, у аэропорта DMK", d="Don Mueang"),
]

ALERT = ("<b>27 сентября: дождь ослаб, но восток ещё в воде.</b> За сутки к утру выпало до 85 мм (Саймай), днём "
         "раньше было 210 мм. Из 80 затопленных участков дорог 41 уже освободился. Каналы Саенсэп, Правет, Латпхрао и "
         "Премпрачакон всё ещё на «красном» уровне, в общинах Кхеха Ромклао (Латкрабанг) и Кхлонг Чан (Бангкапи) вода "
         "около 1 м и выше. Губернатор: главные дороги придут в норму за 2–3 дня, общины — примерно за 2 недели."
         "<span class=\"src\">Источники: BMA, ONWR, TMD, Thai PBS, Thansettakij, Daily News</span>")

NEWS_AT = "27.09, ~11:00"  # time of the latest news summary (BMA, DDPM, media); updated at the morning run


def _stamp():
    """time of the latest automatic update, the news summary and the number of forecast systems used"""
    import json, os
    m = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'model_out.json')))
    agg = m.get('agg') or {}
    f = agg.get('fetched') or ''

    def pl(n, one, few, many):
        return f"{n} " + (one if n % 10 == 1 and n % 100 != 11 else few if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else many)
    ne = sum(1 for r in agg.get('rows', []) if r.get('kind') == 'ens')
    nd = sum(1 for r in agg.get('rows', []) if r.get('kind') == 'det')
    upd = f"Обновлено {f[8:10]}.{f[5:7]} в {f[11:16]} по Бангкоку · " if f else ''
    return (upd + f"сводки на {NEWS_AT} · {pl(ne, 'ансамбль', 'ансамбля', 'ансамблей')} и "
            f"{pl(nd, 'модель', 'модели', 'моделей')} · дождемеры и датчики ThaiWater")

NEWS = [
    dict(when="24–25.09", text="С 16:00 24.09 начались ливни: к утру 25.09 на востоке до 101,5 мм, за 48 часов до 274,5 мм (Минбури). 25.09 Нонгчок, Суанлуанг и Кханнаяо объявлены зоной бедствия."),
    dict(when="ночь 26.09", text="Ливень над центром и севером: больше 200 мм за сутки на пяти станциях (Чатучак 210 мм). Утром 44 затопленных участка и 7 непроезжих точек; все 50 районов объявлены зоной бедствия."),
    dict(when="26.09, вечер", text="Дождь ослаб. В 17:43 — 135 точек подтопления в 31 районе, вечером 33 дороги, которые советовали объезжать. В Кхеха Ромклао (Латкрабанг) отключили свет."),
    dict(when="ночь 27.09", text="Перед рассветом дождь вернулся, но без 200-мм ливня: за сутки к 07:00 — Саймай 85, Нонгчок 83, Донмыанг 71 мм."),
    dict(when="27.09, утро", text="Из 80 участков дорог, затопленных с 24.09, 41 освободился, 39 ещё в воде (в основном 15–20 см); BMA советует объезжать 31 дорогу. В центре — Сиам, Силом, Чайнатаун, Каосан — подтоплений нет, Экамай высыхает."),
    dict(when="восток", text="Каналы Саенсэп, Правет, Латпхрао и Премпрачакон на «красном» уровне: вода прибывает быстрее, чем её откачивают. Воду гонят с востока на запад в Чао Прайю. Губернатор: дороги — через 2–3 дня, общины — примерно через 2 недели."),
    dict(when="река", text="Сброс плотины Чао Прайя — 1 950 м³/с; RID допускает повышение до 2 000–2 300 м³/с, пик стока ждут 27–29.09. Накхонсаван (C.2) — 1 846 м³/с."),
    dict(when="прогноз", text="TMD (предупреждение №14, 27.09): дождь ослабевает, но местами ещё сильный. С 28.09 по 2.10 депрессия уходит в Мьянму и слабеет. Штормов, которые заденут Таиланд в ближайшие 2 недели, пока не видно."),
    dict(when="транспорт", text="Аэропорты работают. TAT: в Суварнабхуми закладывать 3 часа на международный рейс и ехать не через Латкрабанг, а по M7 или Бурапха Витхи; в Донмыанге временно нет такси по счётчику. BTS, MRT и Airport Rail Link ходят, Red Line восстановлена."),
    dict(when="итог", text="В Бангкоке 3 погибших: удар током в Бангкапи и двое утонувших. В пунктах размещения около 4 200 человек. 28.09 школы BMA закрыты, госслужащим рекомендована удалёнка 28–29.09."),
]

ADVICE = [
    dict(tag="жильё", title="Где жить", html="<p>Центр дренируется за часы: Силом и Сатхон, Сиам и Пратунам, нижний Сукхумвит (Нана — Асок — Пхромпхонг), восточный берег у реки. До середины октября не бери отели на востоке: Латкрабанг (в том числе «рядом с аэропортом»), Минбури, Бангкапи, Кхлонгсамва, Нонгчок.</p><p>Бери отель в 5–7 минутах от станции BTS или MRT: в ливень метро едет, такси — нет.</p>"),
    dict(tag="1–2 октября", title="Прилёт", html="<p>29.09–1.10 по ансамблям почти сухо: к прилёту центр без воды, северные окраины высыхают, восток ещё откачивают.</p><p>Из Суварнабхуми — Airport Rail Link до Makkasan или Phaya Thai. На такси — по трассе M7 или Бурапха Витхи, не через Латкрабанг: там вода продержится примерно до 10 октября. За 2–3 дня до вылета проверь прогноз.</p>"),
    dict(tag="каждый день", title="Как передвигаться", html="<ul><li>Грозы в октябре чаще после 15–16 часов. Музеи и прогулки ставь на утро.</li><li>Не заходи в воду: удар током (как в Бангкапи 26.09), открытые люки, лептоспироз.</li><li>Сандалии, дождевик, гермочехол для телефона. Вечером держись метро.</li></ul>"),
    dict(tag="река", title="Набережная и лодки", html="<p>28.09–2.10 и 12–15.10 сильные приливы, пик — утром, около 6–9 часов, а сток Чао Прайи высокий. Пирсы и низкие берега вне дамб (Тхевет, Пхранакхон, Кхлонгсан, Бангкхолэм) могут заливать в часы прилива, речные трамваи иногда отменяют.</p><p>Сам центр за дамбой высотой 2,8–3 м: по оценке, река останется на 0,6–0,8 м ниже.</p>"),
    dict(tag="контакты", title="Куда смотреть", html="<ul><li>BMA: <b>1555</b>, туристическая полиция: <b>1155</b>, TAT: <b>1672</b>, скорая: <b>1669</b>.</li><li>Жалобы и карта подтоплений: Traffy Fondue в LINE.</li><li>Прогноз и радар: tmd.go.th, weather.bangkok.go.th.</li><li>Включи экстренные оповещения на телефоне: DDPM рассылает Cell Broadcast по районам.</li></ul>"),
    dict(tag="запасной план", title="Если станет хуже", html="<p>Главный риск октября — новая депрессия или шторм с Южно-Китайского моря: TMD называет такие системы типичными для октября. Бери тарифы с бесплатной отменой отеля и переносом рейса.</p><p>Повтор 2011 года эксперты считают маловероятным: сток реки сейчас 1,9–2 тыс. м³/с, в 2011 было 3,7–4,7 тыс.</p>"),
]

METHOD = """<p><b>Что показывает цвет.</b> Типичная глубина воды на пониженных улицах и в сои района в течение дня, а не в каждой точке. Центр дренируется за часы, восток и север — днями: там польдеры, открытые каналы и меньше насосов.</p>
<p><b>Дождь.</b> Суперансамбль: ECMWF ENS (51 сценарий), ECMWF AIFS ENS (51), NOAA GEFS (31), канадский GEPS (21), DWD ICON-EPS (40) и британский MOGREPS-G (18), плюс 9 детерминированных моделей: ECMWF HRES 9 км, AIFS, GFS, ICON, JMA, GEM, ARPEGE, UKMO 10 км, CMA. Всё это — через Open-Meteo, на 6 точек города. У каждой системы свой вес, ECMWF весит больше всех. Дальше горизонта модели сценарий продолжают GEFS и GEPS, сезонный ECMWF SEAS5 (51 сценарий) и климатические аналоги ERA5 1991–2025, уменьшенные на 15%: TMD и ONWR ждут октябрь суше нормы из-за очень сильного Эль-Ниньо. Грозы бьют точечно, поэтому к каждому району добавлен случайный разброс.</p><p><b>Факт.</b> Суточные суммы и сегодняшний дождь берутся с дождемеров ThaiWater: около 130 работающих станций BMA, HII и TMD в Бангкоке, по районам — среднее по ближайшим станциям. Станции, которые давно молчат, отброшены. Сутки у дождемеров — с 07:00 до 07:00, поэтому дождь на сегодня = выпавшее с 07:00 плюс прогноз на часы до полуночи. Уровни каналов и реки, заполнение плотин — тоже ThaiWater; прогноз гроз и наблюдения — TMD; погода в аэропортах — METAR.</p>
<p><b>Вода.</b> Для каждого района — «ведро»: дождь превращается в сток (больше, если почва насыщена), насосы, тоннели и каналы откачивают его с оценочной для района скоростью. Сильный прилив и переполненные каналы откачку тормозят. Для северо-востока и запада добавлен приток с полей соседних провинций. Стартовое состояние — сводки 26–27.09: станции BMA, датчики на дорогах, объявления властей. Дальше каждый день начинается там, где закончил последний прогон вчера, а утренние сводки его поправляют. Осадки 24–26.09 подогнаны под станционные суммы.</p>
<p><b>Река и прилив.</b> Прилив — гармонический анализ уровня моря в устье (Copernicus через Open-Meteo), проверен по таблицам приливов: пик 30.09–1.10. После 1.10 добавлен сезонный подъём уровня Сиамского залива. Сток Чао Прайи — тренд GloFAS, привязанный к свежему расходу ниже плотины Чао Прайя (ThaiWater, станция C.13). Уровень у моста Мемориал — прилив плюс вклад стока; калибровка по ноябрю 2025 года: 2 900 м³/с ≈ 2,1 м.</p>
<p><b>Сценарии.</b> «Вероятно» — медиана по 221 сценарию, «Если повезёт» — 10-й процентиль, «Если не повезёт» — 90-й. Процент в карточке района — доля сценариев с водой на улицах.</p>
<p><b>Ограничения.</b> Это не официальный прогноз. Модель не знает, где именно ударит гроза: 100 мм за два часа над любым районом зальют улицы на несколько часов даже в «сухой» по карте день. Дальше 7–10 дней это вероятности, а не даты. Официальное предупреждение ВМС о приливах на октябрь ещё не вышло; сторонние таблицы дают ещё одно окно высоких приливов около 5–9.10.</p>"""

RIVER_TEXT = ("Сброс плотины Чао Прайя — 1 950 м³/с. Ирригационный департамент (RID) допускает повышение до 2 000–2 300 м³/с, "
              "пик стока ждут 27–29 сентября. Это не 2011 год, тогда было 3 700–4 700 м³/с: у моста Мемориал река останется "
              "на 0,6–0,8 м ниже гребня дамбы. Но в сильные приливы вода выходит на низкие берега вне дамб: 11 общин (~320 домов) "
              "в Дусите, Пхранакхоне, Бангкхолэме, Яннаве, Бангкок-Ное и Кхлонгсане, пирсы речных трамваев.")

SOURCES = [
    dict(name="Thansettakij: 39 из 80 участков дорог ещё в воде, 27.09", url="https://www.thansettakij.com/general-news/669949"),
    dict(name="Thai PBS: осадки за сутки к 07:00 27.09", url="https://www.thaipbs.or.th/news/content/558661"),
    dict(name="Thai PBS: губернатор о дренаже востока, 27.09", url="https://www.thaipbs.or.th/news/content/558666"),
    dict(name="Daily News: общины высохнут примерно за 2 недели", url="https://www.dailynews.co.th/news/6225334/"),
    dict(name="Posttoday: община Кхеха Ромклао, 27.09", url="https://www.posttoday.com/general-news/749417"),
    dict(name="Thailand Plus: сводка ONWR на 07:00 27.09", url="https://www.thailandplus.tv/archives/1059096"),
    dict(name="Thai PBS: план сброса плотины Чао Прайя", url="https://www.thaipbs.or.th/news/content/558631"),
    dict(name="Thai Post: предупреждение TMD №14", url="https://www.thaipost.net/general-news/1077177/"),
    dict(name="TAT News: аэропорты и транспорт, 27.09", url="https://www.tatnews.org/2026/09/weather-and-travel-conditions-in-bangkok-and-surrounding-areas-visitor-information/"),
    dict(name="The Nation: 7 непроезжих точек, 26.09", url="https://www.nationthailand.com/thailand/bangkok/40071509"),
    dict(name="The Nation: зона бедствия во всех 50 районах", url="https://www.nationthailand.com/thailand/bangkok/40071507"),
    dict(name="AFP / Gulf News: Bangkok declares flood disaster", url="https://gulfnews.com/world/asia/bangkok-declares-disaster-in-all-50-districts-as-heavy-rain-triggers-severe-floods-1.500688415"),
    dict(name="Thai PBS: 274,5 мм за 48 ч, насосы 1 200 м³/с", url="https://www.thaipbs.or.th/news/content/558595"),
    dict(name="Thai PBS: датчики уровня воды на дорогах, 26.09", url="https://www.thaipbs.or.th/news/content/558585"),
    dict(name="Bangkok Biz News: станции с 200+ мм за сутки", url="https://www.bangkokbiznews.com/news/news-update/1253626"),
    dict(name="Thai PBS World: Чао Прайя 0,88 м, дамба 3 м", url="https://www.thaipbsworld.com/around-thailand/558539"),
    dict(name="Thai PBS: сброс плотины 1 850 → 1 950 м³/с", url="https://www.thaipbs.or.th/news/content/558580"),
    dict(name="MGR Online: RID, пик в Накхонсаване около 2.10", url="https://mgronline.com/politics/detail/9690000093614"),
    dict(name="Thai PBS: предупреждение TMD №10 на 26–27.09", url="https://www.thaipbs.or.th/news/content/558573"),
    dict(name="Thai Post: 15-дневный прогноз TMD", url="https://www.thaipost.net/general-news/1075243/"),
    dict(name="Daily News: гибель в жилом комплексе Кхлонг Чан", url="https://www.dailynews.co.th/news/6223022/"),
    dict(name="Thansettakij: советы TAT туристам", url="https://www.thansettakij.com/business/tourism/669873"),
    dict(name="MGR Online: перенос рейсов авиакомпаниями", url="https://mgronline.com/business/detail/9690000093912"),
    dict(name="InfoQuest: общины за пределами речной дамбы", url="https://www.infoquest.co.th/2026/641730"),
    dict(name="NOAA CPC: El Niño Advisory, 10.09.2026", url="https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml"),
    dict(name="Open-Meteo: ансамбли, GloFAS, уровень моря", url="https://open-meteo.com/"),
    dict(name="Copernicus GloFAS", url="https://global-flood.emergency.copernicus.eu/"),
    dict(name="OpenStreetMap: границы районов, каналы", url="https://www.openstreetmap.org/"),
    dict(name="geoBoundaries: соседние провинции", url="https://www.geoboundaries.org/"),
    dict(name="Климатические нормы Бангкока (TMD 1991–2020)", url="https://en.wikipedia.org/wiki/Bangkok#Climate"),
]

WEEKS = [
    dict(frm="2026-09-27", to="2026-10-03", title="Пик и спад", trip=False,
         text="Сегодня ещё дожди, с 28.09 слабее, 29.09–1.10 почти сухо. Главные дороги освобождаются к 29–30.09, север — к 1–2.10. Восток (Латкрабанг, Минбури, Нонгчок, Кхлонгсамва, Бангкапи) остаётся в воде. 28.09–2.10 сильные приливы и пик стока реки: набережные вне дамб."),
    dict(frm="2026-10-04", to="2026-10-10", title="Переходный период", trip=True,
         text="Слабые и умеренные дожди, чаще вечером. Восток постепенно осушают: к 8.10, по модели, в воде остаётся только Латкрабанг. В центре лужи после ливней уходят за часы."),
    dict(frm="2026-10-11", to="2026-10-17", title="Хвост сезона", trip=True,
         text="Американский ансамбль GEFS даёт более влажный период 11–16.10, канадский GEPS его не видит: возможны короткие ливни. 12–15.10 сильные приливы, риск для прибрежных общин и пирсов. Депрессию с Южно-Китайского моря будет видно за 5–7 дней."),
    dict(frm="2026-10-18", to="2026-10-25", title="Конец сезона дождей", trip=True,
         text="В 2014–2025 годах TMD объявлял конец сезона дождей между 14.10 и 14.11. Прогноз на эти дни почти целиком климатический; серьёзное подтопление маловероятно."),
]


CANAL_RU = {
    "BKK021": "Латпхрао у Ват Банг Буа (Бангкхен)", "BKK003": "Махасават, Банг Круай — Суан Пхак (Талингчан)",
    "BKK009": "Лам Платхиу (Латкрабанг)", "BKK001": "Латпхрао ниже шлюза Кхлонг 2 (Саймай)",
    "BKK020": "Латпхрао, устье Кхлонг 2 (Латпхрао)", "BKK005": "Пхасичароен у Пхеткасем 69 (Бангкхэ)",
    "AIT001": "Асок (Ваттхана)",
}

SOURCES_EXTRA = [
    dict(name="Copernicus GloFAS", what="расход Чао Прайи, прогноз", detail="51 сценарий, 30 дн.", via="Open-Meteo Flood API"),
    dict(name="Уровень моря в устье", what="приливы", detail="гармонический анализ, 46 дн.", via="Copernicus / Open-Meteo Marine"),
    dict(name="ERA5 1991–2025", what="климатическая норма и аналоги", detail="35 лет, суточные суммы", via="Open-Meteo Archive"),
    dict(name="Сводки BMA, DDPM, RID", what="уровни воды по районам сегодня", detail="Thai PBS, The Nation, Thansettakij и др.", via="СМИ и пресс-службы"),
    dict(name="OpenStreetMap, geoBoundaries", what="границы районов, каналы, река", detail="50 районов, 32 канала", via="Overpass, geoBoundaries"),
]

TRIP = dict(frm="2026-10-01", to="2026-10-20")


def _weeks():
    """weekly cards always start on the model's "today" (data/model_out.json) and end on 25 Oct"""
    import json, os
    from datetime import date, timedelta
    m = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'model_out.json')))
    t0, end = date.fromisoformat(m['days'][m['today']]), date(2026, 10, 25)
    trip0, trip1 = date.fromisoformat(TRIP['frm']), date.fromisoformat(TRIP['to'])
    out, a = [], t0
    for i, w in enumerate(WEEKS):
        if a > end:
            break
        b = end if i == len(WEEKS) - 1 else min(end, a + timedelta(6))
        out.append({'from': a.isoformat(), 'to': b.isoformat(), 'title': w['title'], 'text': w['text'],
                    'trip': a <= trip1 and b >= trip0 and a >= trip0 - timedelta(1)})
        a = b + timedelta(1)
    return out

def _nbsp(x):
    # keep thousands groups together ("1 950" must not wrap)
    import re
    if isinstance(x, str):
        return re.sub(r'(?<=\d) (?=\d{3}(?!\d))', '\u00a0', x)
    if isinstance(x, list):
        return [_nbsp(v) for v in x]
    if isinstance(x, dict):
        return {k: _nbsp(v) for k, v in x.items()}
    return x


def build_content():
    return _nbsp(_build_content())


def _build_content():
    districts = {}
    for en, p in D.items():
        districts[en] = dict(ru=p['ru'], poi=p['poi'], riv=p['riv'],
                             notes=[dict(text=x['text'], kind=x.get('kind', 'obs'), until=x.get('until'), **{'from': x.get('frm')}) for x in NOTES.get(en, [])])
    return dict(
        levels=LEVELS, districts=districts, defaultDistrict="Vadhana",
        trip={'from': TRIP['frm'], 'to': TRIP['to']}, midTrip="2026-10-10",
        hotspots=[dict(name=h['name'], lat=h['lat'], lon=h['lon'], note=h['note'], **{'from': h['frm']}, to=h['to']) for h in HOTSPOTS],
        pois=POIS, provinces=PROVINCES, spots=SPOTS,
        alert=ALERT, stamp=_stamp(), news=NEWS, advice=ADVICE, method=METHOD, riverText=RIVER_TEXT, sources=SOURCES,
        weeks=_weeks(),
        tideHigh=1.85, labelNudge={"Don Mueang": [-16, 8]},
        river=dict(ymin=0.8, ymax=3.0, critical=2.4, thresholds=[dict(v=1.7, label="≈1,7 м — низкие берега вне дамб"), dict(v=2.8, label="2,8–3 м — гребень дамбы BMA")]),
        canalRu=CANAL_RU, sourcesExtra=SOURCES_EXTRA,
        footer="Собрано 26.09.2026 · Карта © участники OpenStreetMap, geoBoundaries · Данные: Open-Meteo, Copernicus GloFAS, BMA, TMD",
    )
