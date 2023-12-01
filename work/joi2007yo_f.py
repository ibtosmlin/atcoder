# https://atcoder.jp/contests/joi2007yo/tasks/joi2007yo_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
b = int(input())
G = [[1] * m for _ in range(n)]

for _ in range(b):
    a, b = map(int1, input().split())
    G[a][b] = 0

dp = [[0] * m for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        # up
        if i+1 < n:
            dp[i+1][j] += dp[i][j] * G[i+1][j]
        if j+1 < m:
            dp[i][j+1] += dp[i][j] * G[i][j+1]
print(dp[-1][-1])
