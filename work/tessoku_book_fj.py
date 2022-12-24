n, m, k = map(int, input().split())
con = [tuple(map(int, input().split())) for _ in range(m)]
goodness = [[0] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(i+1, n+1):
        for u, v in con:
            if i < u < v <= j:
                goodness[i][j] += 1

dp = [[-1] * (k+1) for _ in range(n+1)]
# dp[i][j] iページまで見た時のj章ができている時のつながり数
dp[0][0] = 0
for to in range(1, n+1):
    for fm in range(to):
        for ki in range(1, k+1):
            if dp[fm][ki-1] == -1: continue
            dp[to][ki] = max(dp[to][ki], dp[fm][ki-1] + goodness[fm][to])
print(dp[-1][k])