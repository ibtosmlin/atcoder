# https://atcoder.jp/contests/abc338/tasks/abc338_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
INF = 10**18

n, m = map(int, input().split())
dist = [[INF] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int,input().split())
    u -= 1; v -= 1
    dist[u][v] = w
for i in range(n): dist[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            # if dist[i][k] == INF or dist[k][j] == INF: continue
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

dp = [[INF] * n for _ in range(1<<n)]
for i in range(n):
    dp[1<<i][i] = 0

for s in range(1, 1<<n):
    for fm in range(n):
        if not s >> fm & 1 or dp[s][fm] == INF: continue
        for to in range(n):
            if s >> to & 1 or dist[fm][to] == INF: continue
            ns = s | 1<< to
            if dp[ns][to] > dp[s][fm] + dist[fm][to]:
                dp[ns][to] = dp[s][fm] + dist[fm][to]
ret = min(dp[-1])
if ret == INF:
    print('No')
else:
    print(ret)
