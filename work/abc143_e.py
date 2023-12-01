# https://atcoder.jp/contests/abc143/tasks/abc143_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d
# O((E+V)logV)
from heapq import heapify, heappop, heappush

n, m, l = map(int, input().split())
G = [[] for _ in range(n)]
#リストの作成
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    if c >= l: continue
    G[a].append((b,c))
    G[b].append((a,c))

INF = 10**10
MX = 1000

ret = [None] * n

def dij(s):
    dist = [MX*INF for _ in range(n)]
    que = []
    dist[s] = 0
    heappush(que, (0, s))
    while que:
        v, x = heappop(que)
        cntx, gassx = divmod(v, INF)
        if dist[x] < cntx * INF + gassx: continue
        for y, cost in G[x]:
            cnty = cntx
            gassy = gassx + cost
            if gassy > l:
                gassy = cost
                cnty += 1
            vy = cnty*INF+gassy
            if dist[y] > vy:
                dist[y] = vy
                heappush(que, (vy, y))
    ret[s] = [dist[i] for i in range(n)]
    # print(ret[s])

for s in range(n): dij(s)

q = int(input())
for _ in range(q):
    s, t = map(int1, input().split())
    if ret[s][t]//INF == MX:
        print(-1)
    else:
        print(ret[s][t]//INF)
