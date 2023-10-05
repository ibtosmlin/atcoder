# https://atcoder.jp/contests/abc321/tasks/abc321_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

mod = 998244353
q, k = map(int, input().split())
dp = [0] * (k+1)
dp[0] = 1
for _ in range(q):
    f, x = input().split()
    x = int(x)
    if f == '+':
        for ki in range(x, k+1)[::-1]:
            dp[ki] += dp[ki-x]
            dp[ki] %= mod
    else:
        for ki in range(x, k+1):
            dp[ki] -= dp[ki-x]
            dp[ki] %= mod
    print(dp[k])

