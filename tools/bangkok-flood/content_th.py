# Thai page content: the same map and data as the Russian page for 25 Sep - 15 Oct 2026, written for a Bangkok
# driver. No trip, advice or tourist spots; a destination pin instead. A snapshot of the news as of 2 Oct 2026.
import json
import os
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
TH = os.path.join(HERE, 'th')
FROM, TO = '2026-09-25', '2026-10-15'

LEVELS = [
    dict(name="แห้ง", short="แห้ง", depth="0 ซม.",
         desc="วันปกติในฤดูฝน: หลังฝนตกหนัก น้ำระบายหมดใน 1–2 ชั่วโมง"),
    dict(name="น้ำขังถนนต่ำ", short="น้ำขัง", depth="ไม่เกิน 10 ซม.",
         desc="หลังฝนตก น้ำขังริมถนนและในซอย ระบายได้ในไม่กี่ชั่วโมง เดินผ่านได้"),
    dict(name="น้ำท่วมถนน", short="ถนนน้ำท่วม", depth="10–30 ซม.",
         desc="บางถนนรถเก๋งผ่านไม่ได้ รถติด แท็กซี่และแกร็บอาจไม่รับงาน BTS และ MRT ยังวิ่งปกติ"),
    dict(name="น้ำเข้าบ้าน", short="น้ำเข้าบ้าน", depth="30–60 ซม.",
         desc="น้ำท่วมซอย ลานบ้าน และชั้นล่างของบ้านริมคลอง ขังอยู่หลายวัน ควรเลี่ยงเส้นทางนี้"),
    dict(name="วิกฤต", short="วิกฤต", depth="60+ ซม.",
         desc="น้ำสูงระดับเอวขึ้นไป มีการอพยพ ใช้เรือ ควรอยู่ให้ห่าง"),
]

DEST = dict(label="ปลายทาง: ซ.สุขุมวิท 95", mapLabel="ปลายทาง", addr="252 ซอยสุขุมวิท 95 แขวงบางจาก เขตพระโขนง กรุงเทพฯ 10260",
            sub="Bang Chak Apartment · ห่าง BTS บางจากราว 400 ม.", lat=13.698588, lon=100.60613, district="Phra Khanong")

POIS = [
    dict(name="สุวรรณภูมิ", lat=13.6900, lon=100.7501, air=True),
    dict(name="", lat=13.9126, lon=100.6067, air=True),  # the district label already says ดอนเมือง
    dict(name="พระบรมมหาราชวัง", lat=13.7500, lon=100.4913),
    dict(name="ข้าวสาร", lat=13.7589, lon=100.4974),
    dict(name="สยาม", lat=13.7456, lon=100.5341),
    dict(name="ประตูน้ำ", lat=13.7510, lon=100.5406),
    dict(name="อโศก", lat=13.7373, lon=100.5603),
    dict(name="ทองหล่อ", lat=13.7243, lon=100.5784),
    dict(name="เอกมัย", lat=13.7196, lon=100.5853),
    dict(name="สีลม", lat=13.7286, lon=100.5341),
    dict(name="เยาวราช", lat=13.7400, lon=100.5100),
    dict(name="ไอคอนสยาม", lat=13.7266, lon=100.5103),
    dict(name="เอเชียทีค", lat=13.7045, lon=100.5030),
    dict(name="ตลาดนัดจตุจักร", lat=13.7999, lon=100.5505),
    dict(name="อารีย์", lat=13.7797, lon=100.5446),
    dict(name="อ่อนนุช", lat=13.7057, lon=100.6011),
]

PROVINCES = [
    dict(name="นนทบุรี", lat=13.885, lon=100.43),
    dict(name="ปทุมธานี", lat=13.966, lon=100.72),
    dict(name="สมุทรปราการ", lat=13.585, lon=100.70),
    dict(name="สมุทรสาคร", lat=13.535, lon=100.34),
    dict(name="ฉะเชิงเทรา", lat=13.70, lon=100.925),
]

ALERT = ("<b>5 ต.ค.: กรมอุตุฯ เตือนฝนตกหนักวันนี้และพรุ่งนี้ (5–6 ต.ค.) ระวังน้ำท่วมฉับพลัน</b> ฝั่งตะวันออกยังมีน้ำท่วมขัง "
         "หนักสุดที่ลาดกระบัง (ในซอยถึง 80 ซม.) และหนองจอก กทม. แนะนำรถเล็กเลี่ยงถนนเจ้าคุณทหาร ฉลองกรุง "
         "และถนนลาดกระบังใกล้สนามบิน แม่น้ำเจ้าพระยายังต่ำกว่าตลิ่งราว 1.2 ม. ไม่มีพายุเข้า"
         "<span class=\"src\">ที่มา: Floodboard, กทม., กรมอุตุนิยมวิทยา, กรมชลประทาน</span>")

NEWS_AT = "5 ต.ค. ~07.20 น."

NEWS = [
    dict(when="24–25 ก.ย.", text="ฝนเริ่มตกหนักตั้งแต่ 16.00 น. 24 ก.ย. ถึงเช้า 25 ก.ย. ฝั่งตะวันออกวัดได้สูงสุด 101.5 มม. รวม 48 ชั่วโมงสูงสุด 274.5 มม. (มีนบุรี) วันที่ 25 ก.ย. ประกาศหนองจอก สวนหลวง และคันนายาวเป็นพื้นที่ประสบสาธารณภัย"),
    dict(when="คืน 26 ก.ย.", text="ฝนตกหนักมากในเขตชั้นในและทางตอนเหนือ: 5 สถานีวัดได้เกิน 200 มม. ใน 24 ชั่วโมง (จตุจักร 210 มม.) เช้าวันนั้นมีจุดน้ำท่วม 44 จุด และจุดที่รถผ่านไม่ได้ 7 จุด ทั้ง 50 เขตถูกประกาศเป็นพื้นที่ประสบสาธารณภัย"),
    dict(when="26 ก.ย. เย็น", text="ฝนเบาลง เวลา 17.43 น. มีจุดน้ำท่วม 135 จุดใน 31 เขต ช่วงเย็นมีถนน 33 สายที่แนะนำให้เลี่ยง เคหะร่มเกล้า (ลาดกระบัง) ไฟฟ้าถูกตัด"),
    dict(when="คืน 27 ก.ย.", text="ก่อนรุ่งสางฝนกลับมาตกอีก แต่ไม่หนักถึง 200 มม.: ฝน 24 ชั่วโมงถึง 07.00 น. สายไหม 85 มม. หนองจอก 83 มม. ดอนเมือง 71 มม."),
    dict(when="27 ก.ย. เช้า", text="จากถนน 80 ช่วงที่น้ำท่วมตั้งแต่ 24 ก.ย. น้ำลดแล้ว 41 ช่วง ยังเหลือ 39 ช่วง (ส่วนใหญ่ 15–20 ซม.) กทม. แนะนำให้เลี่ยง 31 เส้นทาง ใจกลางเมือง เช่น สยาม สีลม เยาวราช ข้าวสาร ไม่มีน้ำท่วม เอกมัยเริ่มแห้ง"),
    dict(when="คืน 28 ก.ย.", text="01.00–04.00 น. พายุฝนฟ้าคะนองหนักเหนือสุวรรณภูมิ ฝน 24 ชั่วโมงถึง 07.00 น.: ประตูระบายน้ำคลองแสนแสบ (หนองจอก) 63 มม. คลองประเวศฯ 60 มม. มีนบุรี 55 มม. ดอนเมือง 53.5 มม. กรมอุตุฯ วัดที่สนามบินสุวรรณภูมิได้ 48.8 มม. ใจกลางเมือง 17.3 มม. ท้องฟ้าโปร่งตั้งแต่ 06.00 น."),
    dict(when="28 ก.ย.", text="เช้า: คลองจั่น (บางกะปิ) น้ำสูงราว 1.5 ม. หน้าเดอะมอลล์ บางกะปิรถผ่านไม่ได้ 09.00–13.00 น. ฝนตกอีก ฝน 24 ชั่วโมงไม่เกิน 17 มม. (สายไหม 17.4 บางกะปิและลาดพร้าว 16.8 มม.) เปิดถนนวิภาวดีรังสิตให้รถทุกประเภท ช่วงเย็นคลองจั่นน้ำสูงระดับอก เคหะร่มเกล้าเกิน 1 ม. 21.45 น. ผู้ว่าฯ กทม.: น้ำลดช้า"),
    dict(when="29 ก.ย.", text="แห้งทั้งวัน 05.30 น. กทม.: น้ำขังใน 8 เขตฝั่งตะวันออกและตอนเหนือ แนะนำให้เลี่ยง 23 เส้นทาง เซ็นเซอร์ช่วงกลางวัน: พัฒนาการตัดศรีนครินทร์ 24.7 ซม. ลาดพร้าว 122 15.5 ซม. สะพานสูง: หมู่บ้านนักกีฬาแหลมทองน้ำระดับเอวถึงอก สายไหม: หมู่บ้านคลองถนน 30–80 ซม. 18.45 น. ปภ. ส่งข้อความเตือนภัยเรื่องคลองหกวา 19.54 น. กทม. ยกเลิกประกาศพื้นที่ประสบสาธารณภัยใน 21 เขต"),
    dict(when="30 ก.ย.", text="ฝน 24 ชั่วโมงถึง 07.00 น. เกือบทุกจุด 0 มม. ตั้งแต่ 03.00–04.00 น. เริ่มสูบน้ำออกจากคลองจั่น ในสองชั่วโมงน้ำลดราว 50 ซม. ลาดพร้าวและรามคำแหงน้ำลดชัดเจน ช่วงเย็นถนนลาดพร้าวจากซอย 101 ถึงบางกะปิแห้งแล้ว 14.00–16.00 น. ฝนตกทางตอนเหนือ สายไหม 18.6 มม. คันกั้นน้ำคลองหกวาในสายไหมน้ำล้นข้ามแต่ไม่พัง ได้เสริมแนวแล้ว เคหะร่มเกล้าน้ำลด 10–12 ซม."),
    dict(when="1 ต.ค.", text="กลางคืนไม่มีฝน เช้าคลองจั่นน้ำสูงราว 30 ซม. ช่วงเย็นน้ำลดลง เคหะร่มเกล้าทั้งวันลดลง 20 ซม. 14.00 น. กทม. แจ้งถนนสายหลัก 15 สายมีน้ำขังสูงสุด 40 ซม. ส่วนใหญ่ฝั่งตะวันออก 16.00–19.00 น. ฝนฟ้าคะนองพร้อมลูกเห็บที่รัชดาฯ ลาดพร้าว และโชคชัย 4: จตุจักร 60 มม. ในราว 1 ชั่วโมง ตลิ่งชัน 42.6 มม. (สถานีของ กทม. สูงสุด 91.5 มม.) ภาษีเจริญ 49 มม. ถนนแจ้งวัฒนะหน้าโรงพยาบาลมงกุฎวัฒนะรถติดหนัก ข้อมูล Floodboard: ถนนที่มีน้ำขังเพิ่มเป็น 226 กม. เวลา 21.00 น. จาก 107 กม. ช่วงเช้า"),
    dict(when="2 ต.ค. เช้า", text="กลางคืนไม่มีฝน ข้อมูล Floodboard: ถนนที่มีน้ำขัง 103 กม. เซ็นเซอร์ของ กทม. มีน้ำ 6 จาก 236 จุด ลึกสุด 10 ซม. ยังคงประกาศพื้นที่ประสบสาธารณภัย 29 เขต โรงเรียนใน 15 เขตปิดถึง 2 ต.ค. หนักที่สุดคือหนองจอก: หมู่บ้านฟลอราวิลล์และรอยัลปาร์ควิลล์น้ำสูง 60–90 ซม. ชั้นล่างของบ้านจมน้ำ ลาดกระบัง สะพานสูง ประเวศ และมีนบุรี ในซอยน้ำสูง 30–60 ซม. บางจุดถึง 1 ม. (ตามรายงานของประชาชน)"),
]

RIVER_TEXT = ("กราฟแสดงระดับน้ำเจ้าพระยาที่สะพานพุทธ (ประมาณการ) และระดับน้ำขึ้นสูงสุดที่ปากแม่น้ำ แนวคันกั้นน้ำของ กทม. "
              "สูงราว 2.80 ม. ช่วงน้ำทะเลหนุนสูง ตลิ่งต่ำนอกแนวคันกั้นน้ำ ท่าเรือ และชุมชนริมแม่น้ำอาจมีน้ำท่วม "
              "ปริมาณน้ำล่าสุดดูได้ในหัวข้อค่าจากสถานีตรวจวัดด้านล่าง")

METHOD = """<p><b>สีบนแผนที่</b> คือความลึกของน้ำโดยทั่วไปบนถนนที่ต่ำและในซอยของเขตนั้นตลอดวัน ไม่ใช่ทุกจุดในเขต เขตชั้นในระบายน้ำได้ในไม่กี่ชั่วโมง ส่วนฝั่งตะวันออกและตอนเหนือใช้เวลาหลายวัน เพราะเป็นพื้นที่ลุ่ม มีคลองเปิด และเครื่องสูบน้ำน้อยกว่า</p>
<p><b>ฝน</b> ใช้แบบจำลองพยากรณ์อากาศ 15 ระบบผ่าน Open-Meteo: แบบกลุ่ม 6 ระบบ (ECMWF, ECMWF AIFS, NOAA GEFS, GEPS ของแคนาดา, ICON-EPS ของเยอรมนี, MOGREPS-G ของอังกฤษ) และแบบเดี่ยว 9 ระบบ โดยให้น้ำหนัก ECMWF มากที่สุด เกินช่วงพยากรณ์ใช้แบบจำลองรายฤดู ECMWF SEAS5 และสถิติภูมิอากาศ ERA5 ปี 2534–2568</p>
<p><b>ค่าจริง</b> ฝนรายวันจากสถานีวัดฝน ThaiWater (สสน., กทม., กรมอุตุฯ) แต่ละเขตใช้ค่าเฉลี่ยของสถานีในรัศมีราว 6 กม. ระดับน้ำในคลองและแม่น้ำ และปริมาณน้ำในเขื่อน มาจาก ThaiWater เช่นกัน</p>
<p><b>น้ำในแต่ละเขต</b> คำนวณแบบ "ถังน้ำ": ฝนกลายเป็นน้ำผิวดิน (มากขึ้นเมื่อดินอิ่มน้ำ) แล้วถูกสูบออกด้วยเครื่องสูบน้ำ อุโมงค์ และคลอง ตามความสามารถของแต่ละเขต น้ำทะเลหนุนและคลองที่เต็มทำให้ระบายช้าลง ทุกเช้าปรับค่าตามรายงานของ กทม. ปภ. ข่าว และ Floodboard/Traffy Fondue</p>
<p><b>แม่น้ำและน้ำทะเลหนุน</b> น้ำขึ้นน้ำลงคำนวณจากระดับน้ำทะเลที่ปากแม่น้ำ (Copernicus) ปริมาณน้ำเจ้าพระยาใช้แนวโน้มจาก GloFAS ผูกกับค่าวัดจริงท้ายเขื่อนเจ้าพระยา (สถานี C.13 ของกรมชลประทาน)</p>
<p><b>ข้อจำกัด</b> นี่ไม่ใช่การพยากรณ์อย่างเป็นทางการ แบบจำลองไม่รู้ว่าพายุฝนจะตกตรงไหน ฝน 100 มม. ใน 2 ชั่วโมงทำให้ถนนในเขตใดก็ได้มีน้ำท่วมหลายชั่วโมง แม้แผนที่จะแสดงว่าแห้ง การพยากรณ์ล่วงหน้าเกิน 7–10 วันเป็นเพียงความน่าจะเป็น</p>"""

WEEKS = [
    dict(title="7 วันข้างหน้า", text=""),
    dict(title="สัปดาห์ถัดไป", text=""),
]

JUMPS = [dict(day="2026-10-05", label="5–6 ต.ค. เตือนฝนหนัก")]

SOURCES_EXTRA = [
    dict(name="Copernicus GloFAS", what="ปริมาณน้ำเจ้าพระยา (พยากรณ์)", detail="51 ฉากทัศน์ 30 วัน", via="Open-Meteo Flood API"),
    dict(name="ระดับน้ำทะเลที่ปากแม่น้ำ", what="น้ำขึ้นน้ำลง", detail="วิเคราะห์ฮาร์มอนิก 46 วัน", via="Copernicus / Open-Meteo Marine"),
    dict(name="ERA5 2534–2568", what="ค่าปกติและสถิติภูมิอากาศ", detail="35 ปี ฝนรายวัน", via="Open-Meteo Archive"),
    dict(name="รายงาน กทม. ปภ. กรมชลประทาน", what="ระดับน้ำรายเขตในแต่ละวัน", detail="Thai PBS, The Nation, ฐานเศรษฐกิจ ฯลฯ", via="สื่อและหน่วยงาน"),
    dict(name="OpenStreetMap, geoBoundaries", what="ขอบเขตเขต คลอง แม่น้ำ", detail="50 เขต 32 คลอง", via="Overpass, geoBoundaries"),
]

# Thai names for labels that the shared data feeds carry in Russian
DAM_NAMES = {"Пхумипон": "เขื่อนภูมิพล", "Сирикит": "เขื่อนสิริกิติ์", "Пасак Чоласит": "เขื่อนป่าสักชลสิทธิ์",
             "Кхвэной": "เขื่อนแควน้อยบำรุงแดน"}
TMD_STATIONS = {"Аэропорт Суварнабхуми": "ท่าอากาศยานสุวรรณภูมิ", "Бангкок (центр)": "กรุงเทพมหานคร",
                "Порт Кхлонгтой": "ท่าเรือคลองเตย", "Бангна": "บางนา", "Аэропорт Донмыанг": "ท่าอากาศยานดอนเมือง"}


def localize_model(m):
    """window the model output to FROM..TO and replace the Russian labels it carries"""
    a, t0 = m['days'].index(FROM), m['today']
    b = max(m['days'].index(TO), min(t0 + 7, len(m['days']) - 1))  # after 15 Oct: today and a week ahead
    assert a <= t0 <= b, (m['days'][t0], FROM, TO)
    nf = b - t0 + 1  # forecast arrays start on "today"
    out = dict(m, days=m['days'][a:b + 1], today=t0 - a, tide=m['tide'][a:b + 1], river=m['river'][a:b + 1])
    out['districts'] = {n: {k: (v[a:b + 1] if isinstance(v, (list, str)) else v) for k, v in d.items()} for n, d in m['districts'].items()}
    c = m['city']
    out['city'] = dict(obs=c['obs'][a:], clim=c['clim'][a:b + 1], mean=c['mean'][:nf], fc={k: v[:nf] for k, v in c['fc'].items()},
                       **{k: c[k][:nf] for k in ('cum_p10', 'cum_p50', 'cum_p90')})
    ag = dict(m['agg'])
    keep = [j for j, col in enumerate(ag['cols']) if FROM <= col <= TO]
    sl = lambda v: [v[j] for j in keep]
    ag.update(cols=sl(ag['cols']), obs=sl(ag['obs']), consensus=sl(ag['consensus']), tmd=sl(ag['tmd']),
              rows=[dict(r, v=sl(r['v']), label=r['label'].replace(' км', ' กม.')) for r in ag['rows']])
    g = dict(ag['gauges'])
    g['river'] = [{k: v for k, v in r.items() if k != 'label'} for r in g['river']]
    g['canals'] = [{k: v for k, v in r.items() if k != 'label'} for r in g['canals']]
    g['dams'] = [dict(r, name=DAM_NAMES.get(r['name'], r['name'])) for r in g['dams']]
    ag['gauges'] = g
    ag['tmd_obs'] = [dict(o, station=TMD_STATIONS.get(o['station'], o['station'])) for o in ag.get('tmd_obs') or []]
    out['agg'] = ag
    return out


def _stamp(m):
    ag = m.get('agg') or {}
    f = ag.get('fetched') or ''
    ne = sum(1 for r in ag.get('rows', []) if r.get('kind') == 'ens')
    nd = sum(1 for r in ag.get('rows', []) if r.get('kind') == 'det')
    mons = ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.']
    upd = f"อัปเดตข้อมูล {int(f[8:10])} {mons[int(f[5:7]) - 1]} {f[11:16]} น. (เวลากรุงเทพฯ) · " if f else ''
    return upd + f"ข่าวถึง {NEWS_AT} · แบบจำลองแบบกลุ่ม {ne} ระบบและแบบเดี่ยว {nd} ระบบ · สถานีวัดของ ThaiWater"


def _weeks(m):
    """7-day cards from the model's "today" to TO"""
    t0, end = date.fromisoformat(m['days'][m['today']]), date.fromisoformat(m['days'][-1])
    out, a = [], t0
    for w in WEEKS:
        if a > end:
            break
        b = min(end, a + timedelta(6))
        out.append({'from': a.isoformat(), 'to': b.isoformat(), 'title': w['title'], 'text': w['text'], 'trip': False})
        a = b + timedelta(1)
    return out


def build_content_th(m):
    """m: the windowed model output (localize_model)"""
    from districts_static import D
    geo = json.load(open(os.path.join(HERE, 'data', 'geo.json'), encoding='utf-8'))
    th = {d['en']: d['th'] for d in geo['districts']}
    notes = json.load(open(os.path.join(TH, 'notes.json'), encoding='utf-8'))
    hotspots = json.load(open(os.path.join(TH, 'hotspots.json'), encoding='utf-8'))
    sources = json.load(open(os.path.join(TH, 'sources.json'), encoding='utf-8'))
    districts = {en: dict(ru=th[en].replace('เขต', '', 1), poi='', riv=p['riv'],
                          notes=[dict(text=x['text'], kind=x.get('kind', 'obs'), until=x.get('until'), **{'from': x.get('from')})
                                 for x in notes.get(en, [])])
                 for en, p in D.items()}
    return dict(
        levels=LEVELS, districts=districts, defaultDistrict=DEST['district'], dest=DEST, jumps=JUMPS,
        hotspots=[h for h in hotspots if h['to'] >= FROM and h['from'] <= TO],
        pois=POIS, provinces=PROVINCES, spots=[],
        alert=ALERT, stamp=_stamp(m), news=NEWS, method=METHOD, riverText=RIVER_TEXT, sources=sources,
        weeks=_weeks(m),
        tideHigh=1.85, labelNudge={"Don Mueang": [-16, 8]},
        river=dict(ymin=0.8, ymax=3.0, critical=2.4, thresholds=[dict(v=1.7, label="≈1.7 ม. — ตลิ่งต่ำนอกแนวคันกั้นน้ำ"),
                                                                 dict(v=2.8, label="2.8–3 ม. — สันคันกั้นน้ำ กทม.")]),
        canalRu={}, sourcesExtra=SOURCES_EXTRA,
        footer="จัดทำ 2 ต.ค. 2569 · แผนที่ © ผู้ร่วมพัฒนา OpenStreetMap, geoBoundaries · ข้อมูล: Open-Meteo, Copernicus GloFAS, ThaiWater, กทม., กรมอุตุนิยมวิทยา",
    )
