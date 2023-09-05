from jinja2 import Template, Environment, FileSystemLoader
import json
import os
from collections import defaultdict
import glob

cwd = os.path.dirname(__file__)
html_file = os.path.join(cwd, '../index.html')
lib_files = glob.glob('./lib/lib/Lib_*.py')

rdata = defaultdict(list)

rdata['segments'] = [('A', '一般アルゴリズム'),
                    ('D', 'データ構造'),
                    ('GB', '二部グラフ'),
                    ('GD', '有向グラフ'),
                    ('GT', '木'),
                    ('G', 'グラフ'),
                    ('N', '整数'),
                    ('M', '行列'),
                    ('Q', 'クエリ'),
                    ('SP', '最短距離'),
                     ('Str', '文字列'),
                     ('AL', '幾何'),
                     ('O', 'その他'),
                     ]


for filepath in sorted(lib_files):
    if 'Lib_templete.py' in filepath: continue
    x = os.path.basename(filepath)
    y = x.split("_")[1]
    f = open(filepath, 'r')
    flist = [fi.replace('\n', "") for fi in f.readlines()]
    now = None
    title = []
    subtitle = []
    for fi in flist:
        if fi in ['#title#', '#subtitle#', '#name#']:
            now = fi.replace('#', '')
            continue
        if now == 'name': break
        fstr = fi[2:]
        if fstr:
            if now == 'title':title.append(fstr)
            if now == 'subtitle': subtitle.append(fstr)
    rdata[y].append((x, title, subtitle))

#テンプレート読み込み
env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'))
template = env.get_template('template.html')

#レンダリングしてhtml出力
rendered_html = template.render(rdata)
with open(html_file, 'w') as f:
    f.write(rendered_html)

print(rendered_html)