INF = float('inf')
m, n, a = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(m)]
dp = [0] * m
ldp = [INF] * (m+1)
rdp = [INF] * (m+1)
for i in range(n):
    ndp = [INF] * m
    for j in range(m):
        pij = P[j][i]
        ndp[j] = min(ndp[j], min(ldp[j], rdp[j]) + pij, dp[j] + pij - a * (i!=0))
    ldp = [INF] * m
    rdp = [INF] * m
    for j in range(m-1):
        ldp[j+1] = min(ldp[j], ndp[j])
    for j in range(1, m)[::-1]:
        rdp[j-1] = min(rdp[j], ndp[j])
    dp = ndp
print(min(dp))