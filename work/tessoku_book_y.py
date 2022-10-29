direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
h, w = map(int, input().split())
c = [input() for _ in range(h)]
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i+1 < h and c[i+1][j] == '.':
            dp[i+1][j] += dp[i][j]
        if j+1 < w and c[i][j+1] == '.':
            dp[i][j+1] += dp[i][j]
print(dp[-1][-1])
