# https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

mod = 1000000007
dp = [0] * 1000001
for i in range(1, 1000001):
    dp[i] = (dp[i-1] + i) % mod
for i in range(1, 1000001):
    dp[i] = dp[i] * i % mod
for i in range(1, 1000001):
    dp[i] = (dp[i] + dp[i-1]) % mod

a = int(input())
b = int(input())
print((dp[b]-dp[a-1])%mod)
