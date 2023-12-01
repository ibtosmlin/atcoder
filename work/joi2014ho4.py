# https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho4
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

from heapq import heapify, heappop, heappush
INF = 10**20

N, M, X = map(int, input().split())
H = [int(input()) for _ in range(N)]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    if H[a] >= w:
        G[a].append((b, w))
    if H[b] >= w:
        G[b].append((a, w))

dist = [INF] * N
que = []
dist[0] = 0
heappush(que, (0, 0))
while que:
    t, i = heappop(que)
    if dist[i] < t: continue
    # hi は 今いる高さ
    hi = max(0, X-t)
    for j, w in G[i]:
        hj = hi - w
        if hj > H[j]: # 木を降りる
            dt = w + hj - H[j]
        elif hj < 0: # 木を昇る
            dt = w + abs(hj)
        else:
            dt = w
        if dist[j] > t + dt:
            dist[j] = t + dt
            heappush(que, (t+dt, j))

t = dist[-1]
h = max(0, X-t)
ret = t + H[-1]-h
print(-1 if t == INF else ret)