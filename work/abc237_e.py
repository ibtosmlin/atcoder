import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
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

from heapq import heapify, heappop, heappush

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


    def get_dist(self, start, goal):

        return self.dist[goal]


    def get_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


##########################################

n, m = map(int, input().split())
h = list(map(int, input().split()))
G = [[] for _ in range(n)]

maxh = max(h)

# 隣接リストの作成
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d = abs(h[a]-h[b])
    if h[a]<h[b]:
        G[b].append((a, 0))
        G[a].append((b, d))
    elif h[a]>h[b]:
        G[b].append((a, d))
        G[a].append((b, 0))
    else:
        G[b].append((a, 0))
        G[a].append((b, 0))

dij = dijkstra(n, G)
F = dij.build(0)

ret = 0
for i in range(n):
    now = h[0]-h[i]
    if now < 0: continue
    ret = max(ret, now - dij.dist[i])
print(ret)
