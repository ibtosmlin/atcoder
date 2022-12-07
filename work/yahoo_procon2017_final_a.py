s = int(input())
n = len(s)
t = 'yahoo'
m = len(t)
INF = 10**9
dp = [[INF] * m for _ in range(n+1)]

for i, si in enumerate(s):
    for j, tj in enumerate(t):
        for k in range(m):
            #dp[i][k] > dp[i+1][]
            if tj == si:
