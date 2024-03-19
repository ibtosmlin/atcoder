# aliasの設定
cp="`pwd`"

init
echo 'update .bash_aliases'
# snippetsの作成
python3 ${cp}/lib/create_snippets.py
echo 'update snippets'
# git.ioの作成
python3 ${cp}/lib/create_html.py
echo 'update html'