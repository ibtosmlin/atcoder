# https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
s = input()
C = [0] + list(map(int, input().split()))
INF = 10**10

dp = [[INF] * (n+1) for _ in range(n+1)]
for l in range(n):
    dp[l][l+1] = C[1]

for l in range(n):
    for r in range(l, n+1):
        if s[l:r] == s[l:r][::-1]:
            dp[l][r] = C[r-l]

for d in range(1, n+1):
    for l in range(n):
        r = l + d
        if r > n: break
        for k in range(l, r):
            dp[l][r] = min(dp[l][r], dp[l][k]+dp[k][r])

print(dp[0][n])
