import json
import os
from collections import defaultdict


cwd = os.path.dirname(__file__)
snippets_file = os.path.join(cwd, '../.vscode/kyopro.code-snippets')
lib_files = os.path.join(cwd, 'lib')

# \libの中のファイルをすべて取り込む
d = defaultdict(dict)
for file in os.listdir(lib_files):
    if file == 'Lib_templete.py': continue
    f = open(os.path.join(lib_files, file), 'r')
    flist = [fi.replace('\n', "") for fi in f.readlines()]
    now = None
    name = None
    for fi in flist:
        if fi in ['#name#', '#prefix#', '#body#', '#description#', '#end#']:
            now = fi.replace('#', '')
        elif now == 'name':
            name = fi[2:]
            d[name]['prefix'] = []
            d[name]['body'] = []
            d[name]['description'] = []

        elif now != 'end':
            if not name: continue
            if now == 'body':
                d[name][now].append(fi)
            else:
                d[name][now].append(fi[2:])
'''
d = {
"スニペット名": {
  "prefix": "短縮語",
  "body": [
      "展開するコード",
      "展開するコード"
  ],
  "description": "スニペットの説明"
}
}
'''

# 書き出し
with open(snippets_file, 'w') as f:
    json.dump(d, f, indent=4, ensure_ascii=False)
