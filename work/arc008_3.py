# https://atcoder.jp/contests/arc008/tasks/arc008_3
import sys; input: lambda _: sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

from heapq import heapify, heappop, heappush
def dijkstra(n, G, start):
    INF = 10 ** 20
    dist = [INF] * n
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, x = heappop(que)
        if d != dist[x]: continue
        for nx in range(n):
            if x == nx: continue
            nd = d + G[x][nx]
            if nd >= dist[nx]: continue
            dist[nx] = nd
            heappush(que, (nd, nx))
    return dist

##########################################
n = int(input())
pt = [tuple(map(int, input().split())) for _ in range(n)]
INF = 10 ** 20
G = [[INF] * n for _ in range(n)]
for a in range(n):
    xa, ya, ta, _ = pt[a]
    for b in range(n):
        if a == b: continue
        xb, yb, _, rb = pt[b]
        v = min(ta, rb)
        c = ((xa-xb)**2 + (ya-yb)**2) ** 0.5 / v
        G[a][b] = c

ret = dijkstra(n, G, 0)
ret.sort(reverse=True)
ret = ret[:-1]
if ret:
    print(max([ri + i  for i, ri in enumerate(ret)]))
else:
    print(0)
