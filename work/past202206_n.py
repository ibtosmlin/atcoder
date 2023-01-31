# https://atcoder.jp/contests/past202206-open/tasks/past202206_n
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()

# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d
# O((E+V)logV)
class dijkstra:
    def __init__(self, n, G):
        self.INF = INF
        self.n = n                  # ノード数
        self.G = G                  # 有向グラフ
        self.start = None           # 始点
        self.G_used = [None] * n    # 最短経路木の親
        self.dist = [self.INF] * n  # 始点からの距離
        self.count = [0] * n        # 始点からの最短到達パス数

    def build(self, start):
        self.start = start
        self.G_used = [None] * self.n
        self.dist = [self.INF] * self.n
        self.count = [0] * self.n
        next_q = []
        if type(start) is int:
            start = [start]
        for st in start:
            self.dist[st] = 0
            self.count[st] = 1
            next_q.append((st, 0))
        heapify(next_q)
        while next_q:
            x, d = heappop(next_q)
            if self.dist[x] < d: continue
            for nx, d_nx_x in self.G[x]:
                # 変則的な距離の場合はここを調整 ##
                nd = self.dist[x] + d_nx_x
                ############################
                if self.dist[nx] < nd: continue
                if self.dist[nx] == nd:
                    self.count[nx] += self.count[x]
                    continue
                self.dist[nx] = nd
                self.G_used[nx] = x
                self.count[nx] = self.count[x]
                heappush(next_q, (nx, nd))


    def get_dist(self, goal):
        # 各ノードへの最短距離
        return self.dist[goal]


    def get_count(self, goal):
        # 各ノードへの最短距離のパス数
        return self.count[goal]


    def get_path(self, goal):
        # 各ノードへの最短パス
        path = []
        node = goal
        while node != None:
            path.append(node)
            node = self.G_used[node]
        return path[::-1]

##########################################

h, w = map(int, input().split())
N = h * w
def p(i, j):
    return i * w + j
C = [0] * (N+2)
for i in range(h):
    ci = list(map(int, input().split()))
    for j in range(w):
        C[p(i, j)] = ci[j]
C[0] = INF
C[N-1] = INF

G = [[] for _ in range(N+2)]
#リストの作成
for i in range(h):
    for j in range(w):
        x = p(i,j)
        if C[x] == INF: continue
        for di, dj in direc8:
            ni = i + di
            nj = j + dj
            nx = p(ni, nj)
            if notisinhw(ni, nj, h, w):
                if ni == -1 or nj == w:
                    nx = N
                if ni == h or nj == -1:
                    nx = N + 1
            if C[nx] == INF: continue
            G[x].append((nx, C[nx]))
            G[nx].append((x, C[x]))

dij = dijkstra(N+2, G)  #クラスのインスタンス化
dij.build(N)
ret = dij.get_dist(N+1)
print(-1 if ret == INF else ret)

ret = [['.'] * w for _ in range(h)]
for pos in dij.get_path(N+1):
    if pos >= N: continue
    i, j = divmod(pos, w)
    ret[i][j] = '#'
for ri in ret:
    print(''.join(map(str, ri)))