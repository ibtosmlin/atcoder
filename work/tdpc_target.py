# https://atcoder.jp/contests/tdpc/tasks/tdpc_target
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
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)

def distPtoP(pt1, pt2): return abs(pt1 - pt2)
def distCtoC(c1, c2):
    pt1, r1 = c1; pt2, r2 = c2; R, r, d = max(r1, r2), min(r1, r2), distPtoP(pt1, pt2)
    return d < R-r
    # d > R+r :O o
    # d < R-r: ◎
    # else 交差

n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
c.sort(key=lambda x: sum(x))

dp = [[-INF] for _ in range(n+1)]
dp[0][0] = 0


# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d
# O((E+V)logV)
class dijkstra:
    def __init__(self, n, G):
        self.n = n                  # ノード数
        self.G = G                  # 有向グラフ
        self.start = None           # 始点
        self.G_used = [None] * n    # 最短経路木の親
        self.dist = [INF] * self.n  # 始点からの距離
        self.count = [0] * self.n   # 始点からの最短到達パス数


    def build(self, start):
        self.start = start
        self.G_used = [None] * n
        self.dist = [INF] * self.n
        self.count = [0] * self.n
        next_q = []
        if type(start) is int:
            start = [start]
        for st in start:
            self.dist[st] = 0
            next_q.append((0, st))
        heapify(next_q)
        while next_q:
            cd, cn = heappop(next_q)
            if self.dist[cn] < cd: continue
            for nn, nd in self.G[cn]:
                # 変則的な距離の場合はここを調整 ##
                nd_ = self.dist[cn] + nd
                ############################
                if self.dist[nn] < nd_: continue
                if self.dist[nn] == nd_:
                    self.count[nn] += self.count[cd]
                    continue
                self.dist[nn] = nd_
                self.G_used[nn] = cn
                self.count[nn] = self.count[cd]
                heappush(next_q, (nd_, nn))


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

n, m, t = map(int, input().split())
G = [[] for _ in range(n)]
G_R = [[] for _ in range(n)]    #行きと帰りを分けた（有向グラフ）場合
#リストの作成
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((b,c))
    G[b].append((a,c))
    G_R[b].append((a,c))        #行きと帰りを分けた（有向グラフ）場合

dij = dijkstra(n, G)  #クラスのインスタンス化
dijR = dijkstra(n, G_R)
dij.build(0)
dijR.build(0)

dij.get_dist(n-1)
