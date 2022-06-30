import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()


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

INF = float('inf')
n, m, s, t = map(int, input().split())
s -= 1; t -= 1
edges_Y = [[] for _ in range(n)]
edges_S = [[] for _ in range(n)]

#リストの作成
for _ in range(m):
    u, v, a, b = map(int, input().split())
    u, v = u-1, v-1
    edges_Y[u].append((v, a))
    edges_Y[v].append((u, a))
    edges_S[u].append((v, b))
    edges_S[v].append((u, b))

dijY = dijkstra(n, edges_Y)  #クラスのインスタンス化
dijS = dijkstra(n, edges_S)
dijY.build(s)
dijS.build(t)

now = INF
ret = []
for i in range(n)[::-1]:
    now = min(now, dijY.get_dist(i) + dijS.get_dist(i))
    ret.append(10**15 - now)
for r in ret[::-1]:
    print(r)
