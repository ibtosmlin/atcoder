# aliasファイルの作成
cp ~/atcoder/tool/.bash_aliases ~/.bash_aliases
source ~/.bash_aliases
echo 'update .bash_aliases'
# snippetsの作成
python3 ~/atcoder/lib/create_snippets.py
echo 'update snippets'
# git.ioの作成
#pypy3 ~/atcoder/lib/create_html.py
echo 'update html'