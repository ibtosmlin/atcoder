# https://atcoder.jp/contests/abc328/tasks/abc328_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**20
dp = [[INF] * (N+1)
for i in range(N):
    dp[i][i] = 0
    dp[i][i+1] = abs(A[i]-B[i])
for d in range(2, N):
    for l in range(N):
        r = l+d
        if r > N: break
        for m in range(l, r):
            u = A[m:r] + A[l:m]
            v = B[l:r]
            nw = 0
            for x, y in zip(u, v):
                nw += abs(x-y)
            dp[l][r] = min(dp[l][r], nw+C, dp[l][m]+dp[m][r])

print(dp[0][N])
print(dp)