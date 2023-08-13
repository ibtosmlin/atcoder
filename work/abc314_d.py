# https://atcoder.jp/contests/abc314/tasks/abc314_d
import sys
input=lambda _:sys.stdin.readline().rstrip()
mod = 1000000007; mod1 = 998244353

for i in range(1, 20):
    x = pow(i, -1, mod)
    y = pow(i, mod-2, mod)
    print(x, y, x==y)