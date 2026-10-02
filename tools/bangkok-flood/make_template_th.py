"""Derive template_th.html (Thai page to share) from template.html.

The Thai page shows the same map and data for a fixed window, without the traveller's trip, advice and tourist
spots, and marks a destination address. Run after editing template.html, then build_th.py.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()


def rep(old, new, count=1):
    global src
    n = src.count(old)
    assert n == count, (n, old[:100])
    src = src.replace(old, new)


# ---------------- head, fonts ----------------
rep('<title>Паводок в Бангкоке</title>', '<title>แผนที่น้ำท่วมกรุงเทพฯ</title>')
rep('<meta name="description" content="Карта подтоплений Бангкока по 50 районам: что уже в воде и что вероятно до 25 октября 2026 года. Ползунок времени, осадки, приливы, уровень Чао Прайи.">',
    '<meta name="description" content="แผนที่น้ำท่วมกรุงเทพฯ ราย 50 เขต 25 ก.ย. – 15 ต.ค. 2569: น้ำท่วมตรงไหนแล้ว และตรงไหนมีโอกาสท่วม พร้อมฝน น้ำทะเลหนุน และระดับแม่น้ำเจ้าพระยา">')
rep('family=Fira+Sans+Extra+Condensed:wght@500;600;700&family=Golos+Text:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600',
    'family=Kanit:wght@500;600;700&family=Sarabun:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600')
rep('''  --f-display:"Fira Sans Extra Condensed","Roboto Condensed","Arial Narrow",sans-serif;
  --f-body:"Golos Text","Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --f-mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;''',
    '''  --f-display:"Kanit","Sarabun","Leelawadee UI","Noto Sans Thai",sans-serif;
  --f-body:"Sarabun","Leelawadee UI","Noto Sans Thai","Segoe UI",Roboto,Arial,sans-serif;
  --f-mono:"JetBrains Mono","Sarabun",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --dest:#6D28D9;''')
rep('''    --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 28px rgba(0,0,0,.25);
  }
}''', '''    --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 28px rgba(0,0,0,.25);
    --dest:#B79CFF;
  }
}''')
rep('''    --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 28px rgba(0,0,0,.25);
}
*{box-sizing:border-box}''', '''    --shadow:0 1px 2px rgba(0,0,0,.3),0 8px 28px rgba(0,0,0,.25);
    --dest:#B79CFF;
}
*{box-sizing:border-box}''')
# Thai needs room above and below the line for vowels and tone marks
rep('h1{font-family:var(--f-display);font-weight:700;font-size:clamp(40px,6.2vw,72px);line-height:.92;',
    'h1{font-family:var(--f-display);font-weight:700;font-size:clamp(36px,5.6vw,64px);line-height:1.15;')
rep('.dh-date{font-family:var(--f-display);font-weight:700;font-size:30px;line-height:1}',
    '.dh-date{font-family:var(--f-display);font-weight:600;font-size:28px;line-height:1.25}')
rep('.dc-name h3{font-family:var(--f-display);font-weight:700;font-size:28px;margin:0;line-height:1}',
    '.dc-name h3{font-family:var(--f-display);font-weight:600;font-size:28px;margin:0;line-height:1.25}')
rep('.timeline-list li{display:grid;grid-template-columns:86px minmax(0,1fr);',
    '.timeline-list li{display:grid;grid-template-columns:104px minmax(0,1fr);')
rep('#map .hot path{fill:var(--danger);stroke:var(--surface);stroke-width:1.2;vector-effect:non-scaling-stroke}',
    '''#map .hot path{fill:var(--danger);stroke:var(--surface);stroke-width:1.2;vector-effect:non-scaling-stroke}
#map .dest{cursor:pointer}
#map .dest path{fill:var(--dest);stroke:#FFFFFF;stroke-width:1.6;vector-effect:non-scaling-stroke}
#map .dest circle{fill:#FFFFFF}
#map .dest text{font-family:var(--f-body);font-weight:700;fill:var(--ink);paint-order:stroke;stroke:var(--label-halo);stroke-linejoin:round}
.destcard .addr{font-size:14px;color:var(--ink);line-height:1.4}
.destcard .addr small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.destcard .go{align-self:flex-start;border:1px solid var(--dest);color:var(--dest);background:transparent;border-radius:999px;padding:5px 12px;font-size:13px;font-weight:600;cursor:pointer}
.eyebrow,#map .prov,.wk .wd,.srcs th,#hm .grp{letter-spacing:0}''')
rep('''  .weeks{grid-template-columns:repeat(2,minmax(0,1fr))}
  .advice{grid-template-columns:repeat(2,minmax(0,1fr))}''', '''  .weeks{grid-template-columns:repeat(2,minmax(0,1fr))}''')
rep('.weeks{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}',
    '.weeks{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}')

# ---------------- page body ----------------
rep('''      <div class="eyebrow"><span lang="th">น้ำท่วม กรุงเทพฯ</span><span>сезон дождей · 2026</span></div>
      <h1>Паводок <span class="w">в&nbsp;Бангкоке</span></h1>
      <p class="lede">Где вода стоит уже сейчас и где она вероятна до 25 октября, по всем 50 районам. Двигай день на шкале: меняются карта, дождь, прилив в устье и уровень Чао Прайи.</p>''',
    '''      <div class="eyebrow"><span>ฤดูฝน 2569</span><span>25 ก.ย. – 15 ต.ค.</span></div>
      <h1>แผนที่น้ำท่วม <span class="w">กรุงเทพฯ</span></h1>
      <p class="lede">น้ำท่วมตรงไหนแล้ว และตรงไหนมีโอกาสท่วม ครบทั้ง 50 เขต เลื่อนวันที่บนแถบด้านล่าง แผนที่ ปริมาณฝน น้ำทะเลหนุน และระดับแม่น้ำเจ้าพระยาจะเปลี่ยนตาม แตะที่เขตหรือจุดบนแผนที่เพื่อดูรายละเอียด</p>''')
rep('<html lang', '<html lang', 0)
rep('aria-label="Карта подтоплений"', 'aria-label="แผนที่น้ำท่วม"')
rep('aria-label="Сценарий прогноза"', 'aria-label="ฉากทัศน์การพยากรณ์"')
rep('>Если повезёт</button>', '>กรณีดี</button>')
rep('>Вероятно</button>', '>น่าจะเป็น</button>')
rep('>Если не повезёт</button>', '>กรณีแย่</button>')
rep('aria-label="Карта районов Бангкока, цвет показывает уровень подтопления на выбранный день"',
    'aria-label="แผนที่เขตต่าง ๆ ของกรุงเทพฯ สีแสดงระดับน้ำท่วมในวันที่เลือก"')
rep('<button type="button" id="zin" aria-label="Приблизить">+</button>', '<button type="button" id="zin" aria-label="ซูมเข้า">+</button>')
rep('<button type="button" id="zout" aria-label="Отдалить">−</button>', '<button type="button" id="zout" aria-label="ซูมออก">−</button>')
rep('<button type="button" id="zcenter" class="txt" aria-label="Показать центр города">Центр</button>',
    '<button type="button" id="zdest" class="txt" aria-label="ซูมไปที่ปลายทาง" hidden>ปลายทาง</button>\n          <button type="button" id="zcenter" class="txt" aria-label="แสดงใจกลางเมือง">ใจกลาง</button>')
rep('<button type="button" id="zreset" class="txt" aria-label="Показать весь город">Весь</button>',
    '<button type="button" id="zreset" class="txt" aria-label="แสดงทั้งเมือง">ทั้งเมือง</button>')
rep('<button type="button" id="stnBtn" class="txt" aria-pressed="false" aria-label="Показать дождемеры ThaiWater">Датчики</button>',
    '<button type="button" id="stnBtn" class="txt" aria-pressed="false" aria-label="แสดงสถานีวัดฝน ThaiWater">สถานีวัดฝน</button>')
rep('<div class="maphint">Нажми на район · зум: Ctrl + колесо или щипок</div>',
    '<div class="maphint">แตะที่เขตเพื่อดูรายละเอียด · ซูม: Ctrl + ล้อเมาส์ หรือใช้สองนิ้ว</div>')
rep('aria-label="Легенда: уровень воды"', 'aria-label="คำอธิบายสี: ระดับน้ำ"')
rep('''<div class="mapkeys"><span><svg width="12" height="11" aria-hidden="true"><path d="M6 1L11 10H1Z" fill="var(--danger)"/></svg>затопленные участки по сводкам (видны в дни сводок)</span><span><i class="glow"></i>подсветка реки — в прилив заливает берега вне дамб</span><span><i class="dot"></i>аэропорты</span></div>''',
    '''<div class="mapkeys"><span id="destKey" hidden><svg width="11" height="15" viewBox="0 0 22 30" aria-hidden="true"><path d="M11 29C7 23 1 18 1 11a10 10 0 1 1 20 0c0 7-6 12-10 18z" fill="var(--dest)"/><circle cx="11" cy="11" r="4" fill="#fff"/></svg><b id="destKeyT"></b></span><span><svg width="12" height="11" aria-hidden="true"><path d="M6 1L11 10H1Z" fill="var(--danger)"/></svg>จุดน้ำท่วมตามรายงาน (แสดงในวันที่มีรายงาน)</span><span><i class="glow"></i>แม่น้ำเรืองแสง = ช่วงน้ำขึ้น ตลิ่งนอกแนวคันกั้นน้ำอาจท่วม</span><span><i class="dot"></i>สนามบิน</span></div>''')
rep('aria-label="Шкала дней: дождь по дням, норма, прилив"', 'aria-label="แถบวันที่: ฝนรายวัน ค่าปกติ น้ำทะเลหนุน"')
rep('aria-label="Проиграть по дням">▶</button>', 'aria-label="เล่นทีละวัน">▶</button>')
rep('aria-label="Предыдущий день">‹</button>', 'aria-label="วันก่อนหน้า">‹</button>')
rep('aria-label="Следующий день">›</button>', 'aria-label="วันถัดไป">›</button>')
rep('aria-label="Выбор дня"', 'aria-label="เลือกวัน"')
rep('aria-label="Показатели дня"', 'aria-label="ตัวเลขของวัน"')
rep('aria-label="Выбранный район"', 'aria-label="เขตที่เลือก"')
rep('<label for="dsel">Район (твой отель?)</label>', '<label for="dsel">เลือกเขต</label>')
rep('<div class="k">Шанс воды на улицах (10+ см)</div>', '<div class="k">โอกาสน้ำท่วมถนน (10+ ซม.)</div>')
rep('<div class="k">Шанс подтопления домов (30+ см)</div>', '<div class="k">โอกาสน้ำเข้าบ้าน (30+ ซม.)</div>')
rep('aria-label="Уровень воды в районе по дням"', 'aria-label="ระดับน้ำในเขตรายวัน"')
rep('''      <section class="card listcard">
        <h2>Туристические места<small id="spotsDay"></small></h2>
        <div class="rows" id="spots"></div>
      </section>''', '''      <section class="card listcard destcard" id="destcard" hidden>
        <h2>ปลายทาง<small id="destDay"></small></h2>
        <div class="addr" id="destAddr"></div>
        <div class="dc-lv" id="destLv"><span class="t" id="destLvT"></span><span class="dp" id="destLvD"></span></div>
        <svg class="spark" id="destSpark" aria-label="ระดับน้ำในเขตของปลายทางรายวัน"></svg>
        <button type="button" class="go" id="destGo">ดูบนแผนที่</button>
      </section>''')
rep('<h2>Больше всего воды<small id="rankDay"></small></h2>', '<h2>เขตที่น้ำท่วมมากที่สุด<small id="rankDay"></small></h2>')
rep('<h2 class="sec-h" id="rvH">Чао Прайя и прилив</h2>', '<h2 class="sec-h" id="rvH">แม่น้ำเจ้าพระยาและน้ำทะเลหนุน</h2>')
rep('aria-label="График: максимальный прилив в устье и оценка уровня реки у моста Мемориал"',
    'aria-label="กราฟ: ระดับน้ำขึ้นสูงสุดที่ปากแม่น้ำ และระดับแม่น้ำที่สะพานพุทธ (ประมาณการ)"')
rep('<h2 class="sec-h" id="nwH">Что происходит сейчас</h2>', '<h2 class="sec-h" id="nwH">สถานการณ์ล่าสุด</h2>')
rep('''<div class="sec-head"><h2 class="sec-h" id="wkH">Прогноз по неделям</h2><p>Сумма дождя по городу — медиана ансамбля и разброс 10–90%. Норма — среднее за 1991–2025. Тапни неделю, чтобы перейти к её первому дню.</p></div>''',
    '''<div class="sec-head"><h2 class="sec-h" id="wkH">แนวโน้มรายสัปดาห์</h2><p>ปริมาณฝนรวมเฉลี่ยทั้งเมืองจากแบบจำลอง และช่วง 10–90% ค่าปกติคือค่าเฉลี่ยปี 2534–2568 แตะที่สัปดาห์เพื่อไปยังวันแรกของสัปดาห์นั้น</p></div>''')
rep('<h2 class="sec-h" id="agH">Все источники: что говорят модели</h2>', '<h2 class="sec-h" id="agH">แหล่งข้อมูลทั้งหมด: แบบจำลองพยากรณ์ฝนว่าอย่างไร</h2>')
rep('aria-label="Тепловая карта: дождь по городу по дням в каждом источнике"', 'aria-label="ตารางสี: ฝนเฉลี่ยทั้งเมืองรายวันจากแต่ละแหล่ง"')
rep('<summary>Таблица значений</summary>', '<summary>ตารางตัวเลข</summary>')
rep('<h2 class="sec-h" id="lvH">Датчики сейчас</h2>', '<h2 class="sec-h" id="lvH">ค่าจากสถานีตรวจวัดล่าสุด</h2>')
rep('<h3>Каналы Бангкока</h3><div class="sub">Уровень в % от бровки берега, ThaiWater</div>',
    '<h3>คลองในกรุงเทพฯ</h3><div class="sub">ระดับน้ำเป็น % ของระดับตลิ่ง (ThaiWater)</div>')
rep('<h3>Чао Прайя</h3><div class="sub">Расход, м³/с, и уровень, м над уровнем моря</div>',
    '<h3>แม่น้ำเจ้าพระยา</h3><div class="sub">ปริมาณน้ำไหลผ่าน (ลบ.ม./วินาที) และระดับน้ำ (ม.รทก.)</div>')
rep('<h3>Плотины и погода</h3><div class="sub">Заполнение водохранилищ, наблюдения TMD и аэропортов</div>',
    '<h3>เขื่อนและสภาพอากาศ</h3><div class="sub">ปริมาณน้ำในเขื่อน ข้อมูลกรมอุตุฯ และสนามบิน</div>')
rep('<h2 class="sec-h" id="srcH">Подключённые источники</h2>', '<h2 class="sec-h" id="srcH">แหล่งข้อมูลที่ใช้</h2>')
rep('''  <section class="sec" aria-labelledby="advH">
    <div class="sec-head"><h2 class="sec-h" id="advH">Что это значит для поездки</h2></div>
    <div class="advice" id="advice"></div>
  </section>

''', '')
rep('<h2 class="sec-h" id="mH">Как посчитан прогноз</h2>', '<h2 class="sec-h" id="mH">วิธีคำนวณ</h2>')
rep('<h3 class="sec-h" style="font-size:18px;margin-top:4px">Источники</h3>', '<h3 class="sec-h" style="font-size:18px;margin-top:4px">แหล่งข่าวและเอกสารอ้างอิง</h3>')
rep('<span>Не официальный прогноз. Решения принимай по сводкам BMA и TMD.</span>',
    '<span>ไม่ใช่การพยากรณ์อย่างเป็นทางการ ติดตามประกาศของ กทม. (สายด่วน 1555) ปภ. (1784) และกรมอุตุนิยมวิทยา (1182)</span>')

# ---------------- script: dates, numbers ----------------
rep("const MON = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря'];",
    "const MON = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม'];")
rep("const MONS = ['янв','фев','мар','апр','мая','июн','июл','авг','сен','окт','ноя','дек'];",
    "const MONS = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.'];")
rep("const WD = ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'];",
    "const WD = ['วันอาทิตย์','วันจันทร์','วันอังคาร','วันพุธ','วันพฤหัสบดี','วันศุกร์','วันเสาร์'];")
rep("const dLong = i => `${WD[DATES[i].wd]}, ${DATES[i].d} ${MON[DATES[i].m-1]}`;",
    "const dLong = i => `${WD[DATES[i].wd]}ที่ ${DATES[i].d} ${MON[DATES[i].m-1]}`;")
rep("const TRIP0 = idxOf(C.trip.from), TRIP1 = idxOf(C.trip.to);\n", '')
rep("const state = { day: T0, sc: 'p50', sel: store.get('bkkflood.sel') || C.defaultDistrict, playing: false };",
    "const state = { day: T0, sc: 'p50', sel: store.get('bkkflood.th.sel') || C.defaultDistrict, playing: false };")
rep("Number(v).toLocaleString('ru-RU', ", "Number(v).toLocaleString('th-TH', ")

# ---------------- script: destination marker ----------------
rep('''const hots = C.hotspots.map(hs => {''', '''const DEST = C.dest || null;
let destG = null, destPin = null, destDot = null, destTxt = null, DXY = [0, 0];
if (DEST) {
  DXY = proj(DEST.lon, DEST.lat);
  destG = el('g', {class: 'dest', role: 'button', 'aria-label': DEST.label}, map);
  destPin = el('path', {d: ''}, destG);
  destDot = el('circle', {cx: DXY[0], cy: DXY[1], r: 1}, destG);
  destTxt = el('text', {'dominant-baseline': 'middle'}, destG);
  destTxt.textContent = DEST.mapLabel || DEST.label;
  const ttl = el('title', {}, destG); ttl.textContent = DEST.label + ' — ' + DEST.addr;
  destG.addEventListener('click', () => selectDistrict(DEST.district, true));
}
const hots = C.hotspots.map(hs => {''')
rep('''  hots.forEach(o => o.pth.setAttribute('d', `M${o.x} ${o.y - hr}L${o.x + hr * 0.9} ${o.y + hr * 0.62}L${o.x - hr * 0.9} ${o.y + hr * 0.62}Z`));
}''', '''  hots.forEach(o => o.pth.setAttribute('d', `M${o.x} ${o.y - hr}L${o.x + hr * 0.9} ${o.y + hr * 0.62}L${o.x - hr * 0.9} ${o.y + hr * 0.62}Z`));
  if (destG) {
    const r = 8 / s, [x, y] = DXY, cy = y - 1.75 * r;
    destPin.setAttribute('d', `M${x} ${y}C${x - 0.55 * r} ${y - 0.8 * r} ${x - r} ${y - 1.15 * r} ${x - r} ${cy}A${r} ${r} 0 1 1 ${x + r} ${cy}C${x + r} ${y - 1.15 * r} ${x + 0.55 * r} ${y - 0.8 * r} ${x} ${y}Z`);
    destDot.setAttribute('cy', cy); destDot.setAttribute('r', (0.4 * r).toFixed(2));
    destTxt.setAttribute('x', (x + 1.25 * r).toFixed(2)); destTxt.setAttribute('y', cy.toFixed(2));
    destTxt.setAttribute('font-size', (12.5 / s).toFixed(2)); destTxt.setAttribute('stroke-width', (3.2 / s).toFixed(2));
    map.appendChild(destG);
  }
}''')
rep('''$('#zreset').addEventListener('click', () => { view = {x: 0, y: 0, w: VB[2], h: VB[3]}; applyView(); });''',
    '''$('#zreset').addEventListener('click', () => { view = {x: 0, y: 0, w: VB[2], h: VB[3]}; applyView(); });
function zoomDest(){
  if (!DEST) return;
  view.w = VB[2] / 4.5; view.h = view.w * VB[3] / VB[2]; view.x = DXY[0] - view.w / 2; view.y = DXY[1] - view.h / 2; clampView(); applyView();
}
if (DEST) { $('#zdest').hidden = false; $('#zdest').addEventListener('click', () => { zoomDest(); selectDistrict(DEST.district); }); }''')

# ---------------- script: hover tip ----------------
rep("(i >= T0 ? `<div style=\"color:var(--muted);font-size:12px;margin-top:2px\">вода на улицах: ${pr2(n, i)}%</div>` : '');",
    "(i >= T0 ? `<div style=\"color:var(--muted);font-size:12px;margin-top:2px\">โอกาสน้ำท่วมถนน: ${pr2(n, i)}%</div>` : '');")

# ---------------- script: timeline ----------------
rep('''  // trip band
  el('rect', {x: padL + TRIP0 * bw, y: top - 12, width: (TRIP1 - TRIP0 + 1) * bw, height: plotH + 12, class: 'trip'}, tl);
  const tt = el('text', {x: padL + TRIP0 * bw + 4, y: top - 3, class: 'trip-t'}, tl); tt.textContent = small ? 'поездка' : 'твоя поездка';
''', '')
rep("const u = el('text', {x: padL - 4, y: top - 5, 'text-anchor': 'end'}, tl); u.textContent = 'мм';",
    "const u = el('text', {x: padL - 4, y: top - 5, 'text-anchor': 'end'}, tl); u.textContent = 'มม.';")
rep("const t = el('text', {x: x + bw / 2, y: top - 3 + (i === TRIP0 ? 0 : 0), 'text-anchor': 'middle', class: 'vlab'}, tl);",
    "const t = el('text', {x: x + bw / 2, y: top - 3, 'text-anchor': 'middle', class: 'vlab'}, tl);")
rep("const mark = small ? (dd === 1 || i === 0 || (dd % 10 === 0 && dd <= 20)) : (dd === 1 || i === 0 || (dd % 5 === 0 && dd <= 25));",
    "const mark = small ? (dd === 1 || i === 0 || dd % 5 === 0) : (dd === 1 || i === 0 || (dd % 5 === 0 && dd <= 25) || i === N - 1);")
rep("tl2.textContent = small ? '▲ прилив ≥ ' + fmt(C.tideHigh, 2) + ' м' : '▲ сильный прилив (≥ ' + fmt(C.tideHigh, 2) + ' м)   полоса — доля районов с водой на улицах';",
    "tl2.textContent = small ? '▲ น้ำทะเลหนุนสูง ≥ ' + fmt(C.tideHigh, 2) + ' ม.' : '▲ น้ำทะเลหนุนสูง (≥ ' + fmt(C.tideHigh, 2) + ' ม.)   แถบสี = สัดส่วนเขตที่น้ำท่วมถนน';")

# ---------------- script: river chart ----------------
rep("  el('rect', {x: padL + TRIP0 * bw, y: top, width: (TRIP1 - TRIP0 + 1) * bw, height: ph, class: 'trip'}, rv);\n", '')
rep("const u = el('text', {x: 2, y: top + 8}, rv); u.textContent = 'м';", "const u = el('text', {x: 2, y: top + 8}, rv); u.textContent = 'ม.';")
rep("for (let i = 0; i < N; i++) { const dd = DATES[i].d; if (dd === 1 || i === 0 || (dd % 5 === 0 && dd <= 25)) {",
    "for (let i = 0; i < N; i++) { const dd = DATES[i].d; if (dd === 1 || i === 0 || (dd % 5 === 0 && dd <= 25) || i === N - 1) {")
rep("$('#rvKeys').innerHTML = `<span><i style=\"background:var(--ink)\"></i>уровень реки у моста Мемориал (оценка)</span><span><i style=\"background:var(--l2);opacity:.6;height:8px\"></i>если сток будет максимальным</span><span><i style=\"background:var(--river)\"></i>пик прилива в устье</span>`;",
    "$('#rvKeys').innerHTML = `<span><i style=\"background:var(--ink)\"></i>ระดับแม่น้ำที่สะพานพุทธ (ประมาณการ)</span><span><i style=\"background:var(--l2);opacity:.6;height:8px\"></i>กรณีน้ำเหนือมากที่สุด</span><span><i style=\"background:var(--river)\"></i>ระดับน้ำขึ้นสูงสุดที่ปากแม่น้ำ</span>`;")

# ---------------- script: day header and KPIs ----------------
rep("const pill = {fact: '<span class=\"pill fact\">факт</span>', today: '<span class=\"pill today\">сегодня</span>', fc1: `<span class=\"pill fc\">прогноз · день ${i - T0}</span>`, fc2: `<span class=\"pill fc\">прогноз · день ${i - T0}</span>`, clim: `<span class=\"pill clim\">сценарий · день ${i - T0}</span>`}[ph];",
    "const pill = {fact: '<span class=\"pill fact\">ข้อมูลจริง</span>', today: '<span class=\"pill today\">วันนี้</span>', fc1: `<span class=\"pill fc\">พยากรณ์ · อีก ${i - T0} วัน</span>`, fc2: `<span class=\"pill fc\">พยากรณ์ · อีก ${i - T0} วัน</span>`, clim: `<span class=\"pill clim\">แนวโน้ม · อีก ${i - T0} วัน</span>`}[ph];")
rep("const confT = {fact: 'по сводкам BMA и новостям', today: 'сводки утра + прогноз на вечер', fc1: 'надёжность: высокая по дождю, средняя по улицам', fc2: 'надёжность: средняя', clim: 'надёжность: низкая, смесь прогноза и климата'}[ph];",
    "const confT = {fact: 'ตามรายงานของ กทม. และข่าว', today: 'รายงานเช้านี้ + พยากรณ์ช่วงเย็น', fc1: 'ความแม่นยำ: สูงสำหรับฝน ปานกลางสำหรับน้ำบนถนน', fc2: 'ความแม่นยำ: ปานกลาง', clim: 'ความแม่นยำ: ต่ำ (ผสมพยากรณ์กับสถิติภูมิอากาศ)'}[ph];")
rep('<span class="conf" aria-label="надёжность ${conf} из 5">', '<span class="conf" aria-label="ความแม่นยำ ${conf} จาก 5">')
rep("$('#scrubDate').textContent = dLong(i) + (i === T0 ? ' · сегодня' : i === TRIP0 ? ' · прилёт' : i === TRIP1 ? ' · вылет' : '');",
    "$('#scrubDate').textContent = dLong(i) + (i === T0 ? ' · วันนี้' : '');")
rep("const rainS = r.fact ? `факт, среднее по городу · норма ~${fmt(M.city.clim[i])} мм` : (measured != null ? `уже выпало ~${fmtR(measured)} мм · разброс ${fmt(r.lo)}–${fmt(r.hi)}` : `разброс ${fmt(r.lo)}–${fmt(r.hi)} мм · норма ~${fmt(M.city.clim[i])}`);",
    "const rainS = r.fact ? `ค่าจริง เฉลี่ยทั้งเมือง · ค่าปกติ ~${fmt(M.city.clim[i])} มม.` : (measured != null ? `ตกแล้ว ~${fmtR(measured)} มม. · ช่วง ${fmt(r.lo)}–${fmt(r.hi)} มม.` : `ช่วง ${fmt(r.lo)}–${fmt(r.hi)} มม. · ค่าปกติ ~${fmt(M.city.clim[i])}`);")
rep('<div class="kpi"><div class="k">Дождь за день</div><div class="v">${fmt(r.v)}<small>мм</small></div>',
    '<div class="kpi"><div class="k">ฝนทั้งวัน</div><div class="v">${fmt(r.v)}<small>มม.</small></div>')
rep('''<div class="k">Районов с водой на улицах</div><div class="v">${cnt2}<small>из 50</small></div><div class="s">${cnt3 ? `в ${cnt3} — вода во дворах и домах` : 'дома не подтоплены'} · ${Math.round(a2 / aT * 100)}% площади</div>''',
    '''<div class="k">เขตที่น้ำท่วมถนน</div><div class="v">${cnt2}<small>จาก 50</small></div><div class="s">${cnt3 ? `${cnt3} เขต น้ำเข้าบ้าน` : 'ไม่มีเขตที่น้ำเข้าบ้าน'} · ${Math.round(a2 / aT * 100)}% ของพื้นที่</div>''')
rep('''<div class="k">Пик прилива в устье</div><div class="v">${fmt(tide.max, 2)}<small>м</small></div><div class="s">около ${tide.t} · ${tide.max >= C.tideHigh ? 'сильный, реке труднее сбрасывать воду' : 'умеренный'}</div>''',
    '''<div class="k">น้ำทะเลหนุนสูงสุด (ปากแม่น้ำ)</div><div class="v">${fmt(tide.max, 2)}<small>ม.</small></div><div class="s">ราว ${tide.t} น. · ${tide.max >= C.tideHigh ? 'สูง แม่น้ำระบายน้ำได้ช้า' : 'ปานกลาง'}</div>''')
rep('''<div class="k">Чао Прайя у моста Мемориал</div><div class="v">${fmt(riv.lvl, 1)}<small>м</small></div><div class="s">≈ ${fmt(Math.round(riv.q / 50) * 50)} м³/с · ${['спокойно', 'высоко', 'набережные вне дамб в зоне риска', 'угроза перелива'][rr]}</div>''',
    '''<div class="k">เจ้าพระยาที่สะพานพุทธ</div><div class="v">${fmt(riv.lvl, 1)}<small>ม.</small></div><div class="s">≈ ${fmt(Math.round(riv.q / 50) * 50)} ลบ.ม./วินาที · ${['ปกติ', 'สูง', 'ตลิ่งนอกแนวคันกั้นน้ำเสี่ยงท่วม', 'เสี่ยงล้นคันกั้นน้ำ'][rr]}</div>''')
rep('''  renderDistrict();
  renderLists();''', '''  renderDistrict();
  renderDest();
  renderLists();''')

# ---------------- script: district card ----------------
rep("  el('rect', {x: TRIP0 * bw, y: 0, width: (TRIP1 - TRIP0 + 1) * bw, height: 3, style: 'fill:var(--accent)'}, sp);\n", '')
rep("  [[0, 'l'], [TRIP0, 'm'], [N - 1, 'r']].forEach(([k, a]) => {", "  [[0, 'l'], [T0, 'm'], [N - 1, 'r']].forEach(([k, a]) => {")
rep("riv.textContent = `Набережная: в часы прилива (около ${M.tide[i].t}) вода может выходить на низкие участки вне дамбы — пирсы, прибрежные сои и общины. Сам район за дамбой.`;",
    "riv.textContent = `ริมแม่น้ำ: ช่วงน้ำขึ้น (ราว ${M.tide[i].t} น.) น้ำอาจล้นขึ้นบริเวณต่ำนอกแนวคันกั้นน้ำ เช่น ท่าเรือ ซอยริมน้ำ และชุมชนริมแม่น้ำ พื้นที่ส่วนใหญ่ของเขตอยู่หลังคันกั้นน้ำ`;")
rep("$('#dcPoi').textContent = inf.poi ? 'Что здесь: ' + inf.poi : '';", "$('#dcPoi').textContent = inf.poi || '';")
rep('''function row(n, i, extra){''', '''function renderDest(){
  if (!DEST) return;
  const n = DEST.district, i = state.day, L = lvl(n, i);
  $('#destDay').textContent = dShort(i);
  const lv = $('#destLv'); lv.className = 'dc-lv lv' + L;
  $('#destLvT').textContent = `${INFO[n].ru}: ${LV[L].name}`;
  $('#destLvD').textContent = LV[L].depth + (i >= T0 ? ` · โอกาสน้ำท่วมถนน ${pr2(n, i)}%` : '');
  const sp = $('#destSpark'); const W = Math.max(240, Math.round(sp.getBoundingClientRect().width) || 300), H = 46; sp.setAttribute('viewBox', `0 0 ${W} ${H}`); sp.innerHTML = '';
  const bw = W / N;
  for (let k = 0; k < N; k++) el('rect', {x: k * bw, y: 6, width: bw, height: 24, class: 'c', style: `fill:var(--l${lvl(n, k)})`}, sp);
  el('line', {x1: i * bw + bw / 2, x2: i * bw + bw / 2, y1: 4, y2: 32, class: 'm'}, sp);
  el('line', {x1: T0 * bw, x2: T0 * bw, y1: 6, y2: 30, style: 'stroke:var(--accent);stroke-width:2'}, sp);
  [[0, 'l'], [T0, 'm'], [N - 1, 'r']].forEach(([k, a]) => { const t = el('text', {x: a === 'l' ? 0 : a === 'r' ? W : k * bw, y: 43, 'text-anchor': a === 'l' ? 'start' : a === 'r' ? 'end' : 'middle'}, sp); t.textContent = dShort(k); });
}
if (DEST) {
  $('#destcard').hidden = false; $('#destKey').hidden = false; $('#destKeyT').textContent = DEST.label;
  $('#destAddr').innerHTML = `${DEST.addr}${DEST.sub ? `<small>${DEST.sub}</small>` : ''}`;
  $('#destGo').addEventListener('click', () => { zoomDest(); selectDistrict(DEST.district); document.querySelector('.mapcard').scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start'}); });
}
function row(n, i, extra){''')
rep('''  $('#spotsDay').textContent = dShort(i);
  $('#rankDay').textContent = dShort(i);
  const sp = $('#spots'); sp.innerHTML = '';
  C.spots.forEach(s => sp.appendChild(row(s.d, i, s.name)));
''', '''  $('#rankDay').textContent = dShort(i);
''')
rep("function selectDistrict(n, scroll){\n  state.sel = n; store.set('bkkflood.sel', n); renderDistrict();",
    "function selectDistrict(n, scroll){\n  state.sel = n; store.set('bkkflood.th.sel', n); renderDistrict();")
rep("names.slice().sort((a, b) => INFO[a].ru.localeCompare(INFO[b].ru, 'ru'))", "names.slice().sort((a, b) => INFO[a].ru.localeCompare(INFO[b].ru, 'th'))")
rep('''const jumps = [[T0, 'Сегодня'], [TRIP0, 'Прилёт ' + dShort(TRIP0)], [idxOf(C.midTrip), dShort(idxOf(C.midTrip))], [TRIP1, 'Вылет ' + dShort(TRIP1)]];''',
    '''let PEAK = 0, peakN = -1;
for (let i = 0; i <= T0; i++) { let c = 0; names.forEach(n => { if (lvl(n, i, 'p50') >= 2) c++; }); if (c > peakN) { peakN = c; PEAK = i; } }
const jumps = [[T0, 'วันนี้'], [Math.min(N - 1, T0 + 1), 'พรุ่งนี้'], ...(C.jumps || []).map(j => [idxOf(j.day), j.label]).filter(j => j[0] >= 0), [PEAK, 'วันที่ท่วมมากที่สุด · ' + dShort(PEAK)]];''')
rep("function stopPlay(){ if (timer) clearInterval(timer); timer = null; $('#play').textContent = '▶'; $('#play').setAttribute('aria-label', 'Проиграть по дням'); }",
    "function stopPlay(){ if (timer) clearInterval(timer); timer = null; $('#play').textContent = '▶'; $('#play').setAttribute('aria-label', 'เล่นทีละวัน'); }")
rep("$('#play').textContent = '❚❚'; $('#play').setAttribute('aria-label', 'Пауза');", "$('#play').textContent = '❚❚'; $('#play').setAttribute('aria-label', 'หยุด');")

# ---------------- script: weeks ----------------
rep("const card = h('div', {role: 'button', tabindex: '0', class: 'card wk' + (w.trip ? ' trip' : '')});",
    "const card = h('div', {role: 'button', tabindex: '0', class: 'card wk'});")
rep('''card.innerHTML = `<div class="wd">${dShort(a)} — ${dShort(b)}${w.trip ? ' · поездка' : ''}</div><div class="wt">${w.title}</div>
      <div class="wn"><div><b class="num">${fmt(rain)}</b><span>мм дождя (${fmt(Math.max(0, Math.min(cumLo, rain)))}–${fmt(Math.max(cumHi, rain))})</span></div><div><b class="num">${fmt(clim)}</b><span>норма, мм</span></div><div><b class="num">${peak}</b><span>районов с водой в пик</span></div></div>
      <div class="meter" aria-label="Максимальный уровень за неделю по площади города">''',
    '''card.innerHTML = `<div class="wd">${dShort(a)} — ${dShort(b)}</div><div class="wt">${w.title}</div>
      <div class="wn"><div><b class="num">${fmt(rain)}</b><span>มม. ฝนรวม (${fmt(Math.max(0, Math.min(cumLo, rain)))}–${fmt(Math.max(cumHi, rain))})</span></div><div><b class="num">${fmt(clim)}</b><span>ค่าปกติ มม.</span></div><div><b class="num">${peak}</b><span>เขตน้ำท่วมถนน (วันที่มากสุด)</span></div></div>
      <div class="meter" aria-label="ระดับน้ำสูงสุดของสัปดาห์ตามสัดส่วนพื้นที่เมือง">''')
rep('<p>${w.text}</p><p style="color:var(--muted);font-size:12.5px">Сильнейший прилив недели: ${fmt(tmax, 2)} м, ${dShort(tday)}.</p>`;',
    '<p>${w.text}</p><p style="color:var(--muted);font-size:12.5px">น้ำทะเลหนุนสูงสุดของสัปดาห์: ${fmt(tmax, 2)} ม. วันที่ ${dShort(tday)}</p>`;')

# ---------------- script: heatmap ----------------
rep("rows.push({grp: 'Факт и итог'});", "rows.push({grp: 'ค่าจริงและผลรวม'});")
rep("rows.push({id: 'obs', label: 'Факт: дождемеры', bold: true,", "rows.push({id: 'obs', label: 'ค่าจริง: สถานีวัดฝน', bold: true,")
rep("rows.push({id: 'cons', label: 'Итог: консенсус', bold: true,", "rows.push({id: 'cons', label: 'ผลรวม: ค่าฉันทามติ', bold: true,")
rep("rows.push({id: 'tmd', label: 'TMD: % площади с грозами',", "rows.push({id: 'tmd', label: 'กรมอุตุฯ: % พื้นที่มีฝน',")
rep("[['ens', 'Ансамбли, медиана'], ['det', 'Детерминированные модели'], ['seas', 'Сезонный ансамбль']]",
    "[['ens', 'แบบจำลองแบบกลุ่ม (ค่ามัธยฐาน)'], ['det', 'แบบจำลองแบบเดี่ยว'], ['seas', 'แบบจำลองรายฤดู']]")
rep("if (row.id === 'obs') return `<b>${c}${v.partial ? ', пока' : ''}: ${fmtR(v.m)} мм</b>` + (v.partial ? `среднее по ${A.n.today} дождемерам ThaiWater на ${tstamp(A.fetched)}` : 'среднее по городу: дождемеры ThaiWater и сводки BMA');",
    "if (row.id === 'obs') return `<b>${c}${v.partial ? ' ถึงตอนนี้' : ''}: ${fmtR(v.m)} มม.</b>` + (v.partial ? `เฉลี่ยจากสถานีวัดฝน ThaiWater ${A.n.today} แห่ง ณ ${tstamp(A.fetched)}` : 'เฉลี่ยทั้งเมือง: สถานีวัดฝน ThaiWater และรายงาน กทม.');")
rep("if (row.id === 'cons') return `<b>${c}: ${fmtR(v.m)} мм</b>взвешенный консенсус ${A.ntr} сценариев, 10–90%: ${fmtR(v.lo)}–${fmtR(v.hi)} мм`;",
    "if (row.id === 'cons') return `<b>${c}: ${fmtR(v.m)} มม.</b>ค่าฉันทามติถ่วงน้ำหนักจาก ${A.ntr} ฉากทัศน์ ช่วง 10–90%: ${fmtR(v.lo)}–${fmtR(v.hi)} มม.`;")
rep("if (row.id === 'tmd') return `<b>${c}: грозы на ${Math.round(v.pct)}% территории</b>официальный прогноз TMD для Бангкока`;",
    "if (row.id === 'tmd') return `<b>${c}: ฝนฟ้าคะนอง ${Math.round(v.pct)}% ของพื้นที่</b>พยากรณ์ทางการของกรมอุตุฯ สำหรับกรุงเทพฯ`;")
rep("if (v.lo != null) return `<b>${r.label}, ${c}: ${fmtR(v.m)} мм</b>медиана ${r.members} сценариев, 10–90%: ${fmtR(v.lo)}–${fmtR(v.hi)} мм`;",
    "if (v.lo != null) return `<b>${r.label}, ${c}: ${fmtR(v.m)} มม.</b>ค่ามัธยฐานจาก ${r.members} ฉากทัศน์ ช่วง 10–90%: ${fmtR(v.lo)}–${fmtR(v.hi)} มม.`;")
rep("return `<b>${r.label}, ${c}: ${fmtR(v.m)} мм</b>${past ? 'прошедший день, модельный анализ' : 'детерминированный прогноз'}`;",
    "return `<b>${r.label}, ${c}: ${fmtR(v.m)} มม.</b>${past ? 'วันที่ผ่านมา ค่าวิเคราะห์จากแบบจำลอง' : 'พยากรณ์แบบเดี่ยว'}`;")
rep("$('#agSub').textContent = `Дождь в среднем по городу, мм за сутки. ${nEns.length} ансамблей (${nEns.reduce((s, r) => s + r.members, 0)} сценариев) и ${nDet.length} детерминированных моделей; сверху — факт по дождемерам и взвешенный итог. Нажми на клетку, чтобы увидеть разброс.`;",
    "$('#agSub').textContent = `ฝนเฉลี่ยทั้งเมือง มม./วัน จากแบบจำลองแบบกลุ่ม ${nEns.length} ระบบ (${nEns.reduce((s, r) => s + r.members, 0)} ฉากทัศน์) และแบบเดี่ยว ${nDet.length} ระบบ แถวบนสุดคือค่าจริงจากสถานีวัดฝนและผลรวมถ่วงน้ำหนัก แตะที่ช่องเพื่อดูช่วงค่า`;")
rep("$('#hmLegend').innerHTML = '<span class=\"lbl\">мм за сутки</span>'", "$('#hmLegend').innerHTML = '<span class=\"lbl\">มม./วัน</span>'")
rep("$('#hmNote').textContent = `Веса в итоге: ${wtxt}. Дальше горизонта каждой модели сценарий продолжают GEFS и GEPS, сезонный SEAS5 и климат ERA5 (на 15% суше нормы из-за Эль-Ниньо). Пунктир — неполный день.`;",
    "$('#hmNote').textContent = `น้ำหนักในผลรวม: ${wtxt} เกินช่วงพยากรณ์ของแต่ละแบบจำลอง ใช้ GEFS, GEPS แบบจำลองรายฤดู SEAS5 และสถิติภูมิอากาศ ERA5 (แห้งกว่าปกติ 15% เพราะเอลนีโญ) ช่องเส้นประ = ยังไม่ครบวัน`;")
rep("$('#hmTable').innerHTML = '<thead><tr><th>Источник</th>'", "$('#hmTable').innerHTML = '<thead><tr><th>แหล่งข้อมูล</th>'")

# ---------------- script: gauges ----------------
rep("const SIT = {1: 'очень низко', 2: 'низко', 3: 'норма', 4: 'высоко', 5: 'выше берега'};",
    "const SIT = {1: 'ต่ำมาก', 2: 'ต่ำ', 3: 'ปกติ', 4: 'สูง', 5: 'ล้นตลิ่ง'};")
rep("$('#lvSub').textContent = `ThaiWater, TMD и METAR · данные на ${tstamp(A.fetched)} по Бангкоку`;",
    "$('#lvSub').textContent = `ThaiWater กรมอุตุฯ และ METAR · ข้อมูล ณ ${tstamp(A.fetched)} น.`;")
rep("${r.level != null ? ' · ' + fmt(r.level, 2) + ' м' : ''}", "${r.level != null ? ' · ' + fmt(r.level, 2) + ' ม.' : ''}")
rep("}).join('') || '<div class=\"sub\">нет данных</div>';", "}).join('') || '<div class=\"sub\">ไม่มีข้อมูล</div>';", 2)
rep("const v = r.q != null ? `${fmt(Math.round(r.q))} м³/с` : (r.level != null ? `${fmt(r.level, 2)} м` : '—');",
    "const v = r.q != null ? `${fmt(Math.round(r.q))} ลบ.ม./วิ` : (r.level != null ? `${fmt(r.level, 2)} ม.` : '—');")
rep("const sub = [r.level != null ? `уровень ${fmt(r.level, 2)} м` : null, r.bank != null ? `берег ${fmt(r.bank, 2)} м` : null, tstamp(r.time)].filter(Boolean).join(' · ');",
    "const sub = [r.amphoe ? 'อ.' + r.amphoe : null, r.level != null ? `ระดับ ${fmt(r.level, 2)} ม.` : null, r.bank != null ? `ตลิ่ง ${fmt(r.bank, 2)} ม.` : null, tstamp(r.time)].filter(Boolean).join(' · ');")
rep("return `<div class=\"grow\"><div class=\"gn\">${r.label || r.name}<small>${sub}</small></div>",
    "return `<div class=\"grow\"><div class=\"gn\">${r.code ? r.code + ' ' : ''}${r.name}<small>${sub}</small></div>")
rep("const wx = {'-RA': 'слабый дождь', 'RA': 'дождь', '+RA': 'сильный дождь', '-TSRA': 'гроза, слабый дождь', 'TSRA': 'гроза с дождём', '+TSRA': 'сильная гроза', 'TS': 'гроза', 'VCSH': 'ливни рядом', 'VCTS': 'гроза рядом', 'SHRA': 'ливень', '-SHRA': 'слабый ливень', 'BR': 'дымка', 'HZ': 'мгла'};",
    "const wx = {'-RA': 'ฝนเล็กน้อย', 'RA': 'ฝน', '+RA': 'ฝนหนัก', '-TSRA': 'ฝนฟ้าคะนองเล็กน้อย', 'TSRA': 'ฝนฟ้าคะนอง', '+TSRA': 'ฝนฟ้าคะนองหนัก', 'TS': 'ฟ้าคะนอง', 'VCSH': 'มีฝนใกล้เคียง', 'VCTS': 'มีฟ้าคะนองใกล้เคียง', 'SHRA': 'ฝนซู่', '-SHRA': 'ฝนซู่เล็กน้อย', 'BR': 'หมอกบาง', 'HZ': 'ฟ้าหลัว'};\n  const DAMS = C.damNames || {}, TST = C.tmdStations || {};")
rep("const dams = (g.dams || []).map(r => `<div class=\"grow\"><div class=\"gn\">${r.name}<small>приток ${fmt(r.inflow, 1)} · сброс ${fmt(r.release, 1)} млн м³/сут</small></div>",
    "const dams = (g.dams || []).map(r => `<div class=\"grow\"><div class=\"gn\">${DAMS[r.name] || r.name}<small>น้ำไหลเข้า ${fmt(r.inflow, 1)} · ระบาย ${fmt(r.release, 1)} ล้าน ลบ.ม./วัน</small></div>")
rep("${m.icao === 'VTBS' ? 'Суварнабхуми' : 'Донмыанг'}<small>METAR ${m.time.slice(11)}</small></div><div class=\"gv\">${wx[m.wx] || m.wx || 'без осадков'}</div>",
    "${m.icao === 'VTBS' ? 'สนามบินสุวรรณภูมิ' : 'สนามบินดอนเมือง'}<small>METAR ${m.time.slice(11)} น.</small></div><div class=\"gv\">${wx[m.wx] || m.wx || 'ไม่มีฝน'}</div>")
rep("<div class=\"gn\">${o.station}<small>TMD, сутки к ${o.time.slice(11)}</small></div><div class=\"gv\">${fmt(o.rain, 1)} мм</div>",
    "<div class=\"gn\">${TST[o.station] || o.station}<small>กรมอุตุฯ 24 ชม. ถึง ${o.time.slice(11)} น.</small></div><div class=\"gv\">${fmt(o.rain, 1)} มม.</div>")
rep("$('#gDams').innerHTML = dams + met + tobs || '<div class=\"sub\">нет данных</div>';", "$('#gDams').innerHTML = dams + met + tobs || '<div class=\"sub\">ไม่มีข้อมูล</div>';")

# ---------------- script: sources table ----------------
rep("A.rows.forEach(r => rows.push([r.label, r.kind === 'ens' ? 'дождь, ансамбль' : r.kind === 'det' ? 'дождь, детерминированный прогноз' : 'дождь, сезонный ансамбль', r.members > 1 ? `${r.members} сценариев, ${r.horizon} дн.` : `${r.horizon} дн.`, 'Open-Meteo', true]));",
    "A.rows.forEach(r => rows.push([r.label, r.kind === 'ens' ? 'ฝน แบบจำลองแบบกลุ่ม' : r.kind === 'det' ? 'ฝน แบบจำลองแบบเดี่ยว' : 'ฝน แบบจำลองรายฤดู', r.members > 1 ? `${r.members} ฉากทัศน์ ${r.horizon} วัน` : `${r.horizon} วัน`, 'Open-Meteo', true]));")
rep("rows.push(['ThaiWater: дождемеры', 'факт осадков: 24 ч, сегодня, вчера', `${A.n.r24} / ${A.n.today} / ${A.n.yday} станций в Бангкоке`, 'HII, BMA, TMD', ok('thaiwater_rain24') && ok('thaiwater_rain_today')]);",
    "rows.push(['ThaiWater: สถานีวัดฝน', 'ฝนจริง: 24 ชม. วันนี้ เมื่อวาน', `${A.n.r24} / ${A.n.today} / ${A.n.yday} สถานีในกรุงเทพฯ`, 'สสน., กทม., กรมอุตุฯ', ok('thaiwater_rain24') && ok('thaiwater_rain_today')]);")
rep("rows.push(['ThaiWater: каналы и река', 'уровни и расходы', `${(A.gauges.canals || []).length} каналов, ${(A.gauges.river || []).length} станций на реке`, 'HII, RID', ok('thaiwater_waterlevel')]);",
    "rows.push(['ThaiWater: คลองและแม่น้ำ', 'ระดับน้ำและปริมาณน้ำ', `${(A.gauges.canals || []).length} คลอง ${(A.gauges.river || []).length} สถานีริมแม่น้ำ`, 'สสน., กรมชลประทาน', ok('thaiwater_waterlevel')]);")
rep("rows.push(['ThaiWater: водохранилища', 'заполнение, приток, сброс', `${(A.gauges.dams || []).length} плотины`, 'RID, EGAT', ok('thaiwater_dams')]);",
    "rows.push(['ThaiWater: เขื่อน', 'ปริมาณน้ำ น้ำไหลเข้า การระบาย', `${(A.gauges.dams || []).length} เขื่อน`, 'กรมชลประทาน, กฟผ.', ok('thaiwater_dams')]);")
rep("rows.push(['TMD: прогноз на 7 дней', 'официальный прогноз гроз', A.tmd_built ? 'выпуск ' + A.tmd_built.slice(0, 16) : '—', 'TMD Open Data', ok('tmd_forecast')]);",
    "rows.push(['กรมอุตุฯ: พยากรณ์ 7 วัน', 'พยากรณ์ฝนฟ้าคะนองทางการ', A.tmd_built ? 'ออกเมื่อ ' + A.tmd_built.slice(0, 16) : '—', 'TMD Open Data', ok('tmd_forecast')]);")
rep("rows.push(['TMD: наблюдения', 'осадки за сутки', `${(A.tmd_obs || []).length} станций`, 'TMD Open Data', ok('tmd_obs')]);",
    "rows.push(['กรมอุตุฯ: ค่าตรวจวัด', 'ฝน 24 ชม.', `${(A.tmd_obs || []).length} สถานี`, 'TMD Open Data', ok('tmd_obs')]);")
rep("rows.push(['METAR аэропортов', 'погода сейчас', 'VTBS, VTBD', 'aviationweather.gov', ok('metar')]);",
    "rows.push(['METAR สนามบิน', 'สภาพอากาศขณะนี้', 'VTBS, VTBD', 'aviationweather.gov', ok('metar')]);")
rep("$('#srcTable').innerHTML = '<thead><tr><th>Источник</th><th>Что даёт</th><th>Объём</th><th>Через</th><th></th></tr></thead><tbody>'",
    "$('#srcTable').innerHTML = '<thead><tr><th>แหล่งข้อมูล</th><th>ใช้ทำอะไร</th><th>ขนาดข้อมูล</th><th>ผ่าน</th><th></th></tr></thead><tbody>'")
rep("const t = el('title', {}, c); t.textContent = `${sn[4]}: ${sn[2] != null ? fmt(sn[2], 1) + ' мм за 24 ч' : ''}${sn[3] != null ? (sn[2] != null ? ', ' : '') + 'сегодня ' + fmt(sn[3], 1) + ' мм' : ''}${sn[5] ? ' · ' + sn[5] : ''}`;",
    "const t = el('title', {}, c); t.textContent = `${sn[4]}: ${sn[2] != null ? fmt(sn[2], 1) + ' มม. ใน 24 ชม.' : ''}${sn[3] != null ? (sn[2] != null ? ', ' : '') + 'วันนี้ ' + fmt(sn[3], 1) + ' มม.' : ''}${sn[5] ? ' · ' + sn[5] : ''}`;")

# ---------------- static content ----------------
rep("$('#advice').innerHTML = C.advice.map(a => `<div class=\"card adv\"><span class=\"tag\">${a.tag}</span><h3>${a.title}</h3>${a.html}</div>`).join('');\n", '')
rep("function relayout(){ applyView(); buildTimeline(); buildRiver(); renderDistrict(); buildHeatmap(); }",
    "function relayout(){ applyView(); buildTimeline(); buildRiver(); renderDistrict(); renderDest(); buildHeatmap(); }")

out = os.path.join(HERE, 'template_th.html')
open(out, 'w', encoding='utf-8').write(src)
import re
left = sorted(set(re.findall(r'[А-Яа-яЁё][А-Яа-яЁё ,.:;!?«»—–-]*', src)))
print('wrote', os.path.relpath(out, HERE), '· Cyrillic left:', len(left))
for x in left[:40]:
    print('  ', x[:80])
