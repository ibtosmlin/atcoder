#####################################
# 最大正方形
def max_square(h, w, G, block):
    dp = [[0] * w for _ in range(h)]
    mx = 0
    for i in range(h):
        if G[i][0] != block: dp[i][0] = 1; mx = 1
    for j in range(w):
        if G[0][j] != block: dp[0][j] = 1; mx = 1
    for i in range(1, h):
        for j in range(1, w):
            if G[i][j] == block: continue
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp

h, w, n = map(int, input().split())
G = [[0] * w for _ in range(h)]
for _ in range(n):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a][b] = 1

maxsquare = max_square(h, w, G, 1)

dp = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        dp[i][j] = maxsquare[i][j]
        if i != 0:
            dp[i][j] += dp[i-1][j]
        if j != 0:
            dp[i][j] += dp[i][j-1]
        if i != 0 and j != 0:
            dp[i][j] -= dp[i-1][j-1]
print(dp[-1][-1])
