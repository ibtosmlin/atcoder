# https://atcoder.jp/contests/abc310/tasks/abc310_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1
mod = 998244353
n = int(input())
a = list(map(int, input().split()))
a.sort()

p = 1
for ai in a:
    p *= pow(ai, mod-2, mod)
    p %= mod
# dp[i][S]  iまでのサイコロで0から10以下の数を作れるかどうか S & 1<<j == 1なら作れる

def f(x):
    ret = [0] * 11
    for i in range(1, min(x+1, 11)):
        ret[i] = 1
    ret[0] = max(0, x - 10)
    return ret

for i in range(n):
    a[i] = f(a[i])

dp = [[0] * (1<<11) for _ in range(n+1)]
dp[0][1] = 1

for i in range(n):
    ai = a[i]
    for s in range(1<<11):
        if dp[i][s] == 0: continue
        for j, c in enumerate(ai):
            # s: s > i & 1:  i+1が可能
            # jの出目とその回数
            ns = s | 1<<j
            for k in range(11):
                if s >> k & 1 and j + k < 11:
                    ns |= 1 << (j+k)
            dp[i+1][ns] += dp[i][s] * c
            dp[i+1][ns] %= mod

ret = 0
for i in range(1<<11):
    if (i >> 10) & 1:
        ret += dp[-1][i]

print(ret*p%mod)