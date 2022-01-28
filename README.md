# AtCoder 環境
[AtCoder](https://atcoder.jp/) のツール

## Features
- サンプルケースを取得して、テンプレート準備
```console
$ atc https://atcoder.jp/contests/abc234/tasks/abc234_a d
```
- サンプルケースのテストを実行
```console
$ atc https://atcoder.jp/contests/abc234/tasks/abc234_a t
```
- コードを提出(Pypy)
```console
$ atc https://atcoder.jp/contests/abc234/tasks/abc234_a s
```
- コードを提出(Python3)
```console
$ atc https://atcoder.jp/contests/abc234/tasks/abc234_a ss
```

## On contest
- tool/contest_id.txt の中身を変える
```txt
con_root="https://atcoder.jp/contests"
con_id="abc234"
```
- コンテスト中
```console
$ a.py [command]
$ b.py [command]
...
$ h.py [command]
```

## Requirements
[online-judge-tools](https://github.com/kmyk/online-judge-tools)