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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
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
        next_q = []
        for si in start:
            self.dist[si] = 0
            next_q.append((0, si))
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
n, m, k = map(int, input().split())
edges = [[] for _ in range(n)]
#リストの作成
ed = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append((b,c))
    edges[b].append((a,c))
    ed.append((a, b, c))

dij = dijkstra(n, edges)  #クラスのインスタンス化
start = [int1(input()) for _ in range(k)]
dij.build(start)

ret = 0
for i in range(n):
    ret = max(ret, dij.get_dist(i))
for a, b, l in ed:
    ret = max(ret, (dij.get_dist(a) + dij.get_dist(b) + l + 1) // 2)

print(ret)
