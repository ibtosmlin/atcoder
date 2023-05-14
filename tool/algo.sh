#!/bin/sh
arg=${1}
if [ -z "$arg" ]; then
    # aliasファイルの作成
    cp ~/atcoder/tool/template.py ~/atcoder/tool/test.py
    code ~/atcoder/tool/test.py
elif [ $arg = 't' ]; then
    python3 ~/atcoder/tool/test.py
fi