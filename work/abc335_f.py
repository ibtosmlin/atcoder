# https://atcoder.jp/contests/abc335/tasks/abc335_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

mod = 998244353
N = int(input())
A = list(map(int, input().split()))
M = 500

dp = [0] * N
dp[0] = 1

ret = 0
for i in range(N):
    nw = 1
    while i + nw * A[i] < N:
        dp[i + nw * A[i]] += dp[i]
        dp[i + nw * A[i]] %= mod
        nw += 1
    ret += dp[i]
    ret %= mod
print(ret)