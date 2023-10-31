# https://atcoder.jp/contests/abc326/tasks/abc326_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
mod = 998244353
p = pow(n, mod-2, mod)

dp = [0] * (n+1)
rdp = [0] * (n+1)
"""dp[i]: 現在の値がiの時に得られる期待値"""

for i in range(n)[::-1]:
    dp[i] = (rdp[i+1] + a[i]) * p
    dp[i] %= mod
    rdp[i] = rdp[i+1] + dp[i]
    rdp[i] %= mod
print(rdp[0])