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
            nd = taxi[cn][0]
            if self.dist[cn] < cd: continue
            for nn in self.edges[cn]:
                # 変則的な距離の場合はここを調整 ##
                nd_ = cd + nd
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

n, k = map(int, input().split())
taxi = [tuple(map(int, input().split())) for _ in range(n)]
road = [[] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    road[a].append(b)
    road[b].append(a)

edges = [[] for _ in range(n)]

def bfs(st, r, c):
    seen = [-1] * n
    que = deque()
    que.append(st)
    seen[st] = 0
    while que:
        nw = que.popleft()
        for nx in road[nw]:
            if seen[nx]!=-1: continue
            seen[nx] = seen[nw] + 1
            if seen[nx] <= r:
                edges[st].append(nx)
                que.append(nx)
for i in range(n):
    ci, ri = taxi[i]
    bfs(i, ri, ci)

dij = dijkstra(n, edges)  #クラスのインスタンス化
dij.build(0)
ret = dij.get_dist(n-1)
print(ret)
