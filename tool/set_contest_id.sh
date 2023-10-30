echo con_root=\"https://atcoder.jp/contests\" > ~/atcoder/tool/contest_id.txt
echo con_id=\"${1}\" >> ~/atcoder/tool/contest_id.txt
# code ~/atcoder/tool/contest_id.txt

at https://atcoder.jp/contests/${1}/tasks/${1}_g template
at https://atcoder.jp/contests/${1}/tasks/${1}_f template
at https://atcoder.jp/contests/${1}/tasks/${1}_e template
at https://atcoder.jp/contests/${1}/tasks/${1}_d template
at https://atcoder.jp/contests/${1}/tasks/${1}_c template
at https://atcoder.jp/contests/${1}/tasks/${1}_b template
at https://atcoder.jp/contests/${1}/tasks/${1}_a template
