# https://atcoder.jp/contests/abc197/tasks/abc197_f
import sys
from heapq import heapify, heappop, heappush
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()

n, m = map(int, input().split())
G = [dict() for _ in range(n)]
for _ in range(m):
    a, b, c = input().split()
    a = int1(a)
    b = int1(b)
    G[a][c] = G[a].get(c, set()) | {b}
    G[b][c] = G[b].get(c, set()) | {a}

off = n
N = n * (n + 1)
G2 = [[] for _ in range(N+1)]
for i in range(n):
    for j in range(n):
        node = i * off + j
        for c in G[i]:
            if not c in G[j]: continue
            for ni in G[i][c]:
                for nj in G[j][c]:
                    node2 = ni * off + nj
                    G2[node].append((node2, 2))
        if i == j:
            G2[node].append((N, 0))

for i in range(n):
    for jset in G[i].values():
        for j in jset:
            if i == j: continue
            G2[i*off+j].append((N, 1))

INF = 10 ** 9
dist = [INF] * (N+1)
dist[n-1] = 0
que = [(0, n-1)]
heapify(que)
while que:
    w, x = heappop(que)
    for nx, nw in G2[x]:
        if dist[nx] <= w+nw: continue
        dist[nx] = w + nw
        heappush(que, (w+nw, nx))
ret = dist[N]
print(-1 if ret == INF else ret)
