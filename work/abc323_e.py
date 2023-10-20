# https://atcoder.jp/contests/abc323/tasks/abc323_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

mod = 998244353
n, x = map(int, input().split())
T = list(map(int, input().split()))
prov = pow(n, mod-2, mod)

dp = [0] * (x+1)
dp[0] = 1
# dp[i] 曲目まで決めて時刻jまで音楽が確定する確率
for i in range(x+1):
    for k in range(n):
        if i - T[k] >= 0:
            dp[i] += dp[i-T[k]] * prov
            dp[i] %= mod

ret = 0
for xi in range(x+1):
    if dp[xi] and xi + T[0] > x:
        ret += dp[xi] * prov
        ret %= mod
print(ret)
