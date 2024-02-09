# https://atcoder.jp/contests/oupc2023-day1/tasks/oupc2023_day1_k
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

from heapq import heapify, heappop, heappush
n, m = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    a, b, s, t = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, s, t))

INF = 10 ** 20
ret = INF

for b, s, t in G[0]:
    dp = [INF] * n
    que = []
    dp[b] = t
    heappush(que, (t, b))


while que:
    sx, x = heappop(que)
    if dp[x] < sx: continue
    for nx, ns, nt in G[x]:
        if sx > ns: continue
        if dp[nx] <= nt: continue
        dp[nx] = nt
        heappush(que, (nt, nx))

print(-1 if ret == INF else ret)