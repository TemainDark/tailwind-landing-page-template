"""Inline geometry, model output and content into the page template.

Writes:
  public/bangkok-flood/index.html     standalone page (served by the site / any static host)
  data/bangkok-flood.fragment.html    body fragment for publishing as a claude.ai Artifact
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
DATA = os.path.join(HERE, 'data')
OUT = os.path.join(HERE, '..', '..', 'public', 'bangkok-flood', 'index.html')

from content import build_content


def js(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
geo = json.load(open(os.path.join(DATA, 'geo.json'), encoding='utf-8'))
model = json.load(open(os.path.join(DATA, 'model_out.json'), encoding='utf-8'))

for key, val in (('/*__GEO__*/null', geo), ('/*__MODEL__*/null', model), ('/*__CONTENT__*/null', build_content())):
    assert key in tpl, key
    tpl = tpl.replace(key, js(val))

open(os.path.join(DATA, 'bangkok-flood.fragment.html'), 'w', encoding='utf-8').write(tpl)

head, body = tpl.split('</style>', 1)
doc = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + '\n:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}\n'
       'img{max-width:100%}\n</style>\n</head>\n<body>\n' + body.strip() + '\n</body>\n</html>\n')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(doc)
print('wrote', os.path.relpath(OUT, HERE), round(len(doc.encode()) / 1024, 1), 'KB')
