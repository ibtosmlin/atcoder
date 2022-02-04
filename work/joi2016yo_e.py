import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache

from pkg_resources import EggMetadata
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'

# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d
# O((E+V)logV)
class dijkstra:
    def __init__(self, n, edges):
        self.n = n              # ノード数
        self.edges = edges      # 有向グラフ
        self.prev = [-1] * n    # 前のノード
        self.start = None       # 始点

    def build(self, start):
        self.dist = [INF] * self.n
        self.dist[start] = 0
        next_q = [(0, start)]
        heapify(next_q)
        while next_q:
            cd, cn = heappop(next_q)
            if self.dist[cn] < cd: continue
            for nn, nd in self.edges[cn]:
                # 変則的な距離の場合はここを調整 ##
                nd_ = self.dist[cn] + nd
                ############################
                if self.dist[nn] <= nd_: continue
                self.dist[nn] = nd_
                self.prev[nn] = cn
                heappush(next_q, (nd_, nn))


    def get_dist(self, goal):
        return self.dist[goal]


    def get_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


##########################################

n, m, k, s = map(int, input().split())
p, q = map(int, input().split())
c = [int1(input()) for _ in range(k)]
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)
towns = [-1] * n

que = deque([])
for ci in c:
    que.append(ci)
    towns[ci] = 0
while que:
    nw = que.popleft()
    for nx in edges[nw]:
        if towns[nx] != -1: continue
        towns[nx] = towns[nw] + 1
        if towns[nx] < s:
            que.append(nx)

edgesw = [[] for _ in range(n)]
for i in range(n):
    for j in edges[i]:
        if j==n-1 or j==0:
            edgesw[i].append((j, 0))
        elif towns[j] == 0:
            continue
        elif towns[j] == -1:
            edgesw[i].append((j, p))
        else:
            edgesw[i].append((j, q))

dij = dijkstra(n, edgesw)
dij.build(0)
print(dij.get_dist(n-1))
