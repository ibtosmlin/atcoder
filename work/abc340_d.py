import sys; input: lambda _: sys.stdin.readline().rstrip()
from heapq import heappop, heappush
n = int(input())
G = [[] for _ in range(n)]
for i in range(n-1):
    a, b, t = map(int, input().split())
    G[i].append((t-1,b))
    G[i].append((i+1,a))
INF = 10**18
dp=[INF] * n; que = []
dp[0] = 0; heappush(que,(0, 0))
while que:
    d, v = heappop(que)
    for nv, dd in G[v]:
        if dd+d >= dp[nv]: continue
        dp[nv] = dd+d; heappush(que, (dd+d, nv))
print(dp[-1])
