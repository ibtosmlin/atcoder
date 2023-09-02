import json
import os
from collections import defaultdict
import glob

cwd = os.path.dirname(__file__)
snippets_file = os.path.join(cwd, '../.vscode/kyopro.code-snippets')
lib_files = glob.glob('./lib/lib/Lib_*.py')

# \libの中のファイルをすべて取り込む
for i in sorted(lib_files):
    print(i)
