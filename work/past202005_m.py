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
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
#リストの作成
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append((b,1))
    edges[b].append((a,1))

dij = dijkstra(n, edges)  #クラスのインスタンス化
s = int1(input())
k = int(input())
t = list(map(int1, input().split()))
dists = dict()
dij.build(s)
dists[s] = [dij.dist[i] for i in t]
for ti in t:
    dij.build(ti)
    dists[ti] = [dij.dist[i] for i in t]

dp = [[INF] * k for _ in range(1<<k)]
#dp[i][j]:   iに今まで行ったことがあって、今tjにいる
for i, ti in enumerate(t):
    dp[1<<i][i] = dists[s][i]
for i in range(1<<k):
    for fm in range(k):
        for to in range(k):
            if i>>to & 1: continue
            dp[i|(1<<to)][to] = min(dp[i|(1<<to)][to], dp[i][fm] + dists[t[fm]][to])

print(min(dp[-1]))