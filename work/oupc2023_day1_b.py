# https://atcoder.jp/contests/oupc2023-day1/tasks/oupc2023_day1_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
mod = 998244353
s = input()
n = len(s)
dp = [0] * (n+1)
pv = [0, "Z"]
ret = 0
for i in range(n):
    dp[i+1] = dp[i]
    if s[i] == pv[1]:
        dp[i+1] += i - pv[0]
        dp[i+1] %= mod
        pv[0] = i
    pv[1] = s[i]
    ret += dp[i+1]
    ret %= mod

print(ret)