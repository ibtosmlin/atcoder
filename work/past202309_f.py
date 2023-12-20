# https://atcoder.jp/contests/past16-open/tasks/past202309_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
mod = 998244353
s = input() + "*"
ret = 1
now = 0
for si in s:
    if si == '*':
        ret *= now
        ret %= mod
        now = 0
    else:
        now *= 10
        now += int(si)
        now %= mod
print(ret)