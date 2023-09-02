# https://atcoder.jp/contests/abc318/tasks/abc318_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

n = int(input())
D = [[0]*n for _ in range(n)]
for i in range(n-1):
    di = list(map(int, input().split()))
    for j in range(n-1-i):
        D[i][1+j+i] = di[j]
        D[1+j+i][i] = di[j]

dp = [[-1] * (1<<n) for _ in range(n+1)]
dp[0][0] = 0
ret = 0
for i in range(n):
    for s in range(1<<n):
        if dp[i][s] == -1: continue
        for j in range(n):
            if s >> j & 1: continue
            for k in range(j+1, n):
                if s >> k & 1: continue
                to = s | 1<<j | 1<<k
                dp[i+1][to] = max(dp[i+1][to], dp[i][s]+D[j][k])
                ret = max(ret, dp[i+1][to])

print(ret)
