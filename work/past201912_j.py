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
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

edges = [[] for _ in range(h*100+w)]
#リストの作成
for hi in range(h):
    for wi in range(w):
        fm = hi*100+wi
        for dh, dw in [(1,0), (0,1), (-1,0), (0,-1)]:
            nh = hi+dh
            nw = wi+dw
            if not ((0<=nh<h) and (0<=nw<w)): continue
            to = nh*100+nw
            edges[fm].append((to, a[nh][nw]))

dij0 = dijkstra(h*100+w, edges)  #クラスのインスタンス化
dij1 = dijkstra(h*100+w, edges)  #クラスのインスタンス化
dij2 = dijkstra(h*100+w, edges)  #クラスのインスタンス化

to = [(h-1)*100, (h-1)*100+(w-1), w-1]
dij0.build((h-1)*100)
dij1.build(w-1)
dij2.build((h-1)*100+w-1)

ret = INF
for hi in range(h):
    for wi in range(w):
        nw = 0
        nw += dij0.dist[hi*100+wi]
        nw += dij1.dist[hi*100+wi]
        nw += dij2.dist[hi*100+wi]
        nw -= a[hi][wi] * 2
        ret = min(ret, nw)
print(ret)
