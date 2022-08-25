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
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
def distPtoP(pt1, pt2): return dist2(pt1, pt2) ** 0.5
def distCtoC(c1, c2):
    pt1, r1 = c1; pt2, r2 = c2; R, r, d = max(r1, r2), min(r1, r2), dist(pt1, pt2)
    return d-R-r if d > R+r else R-r-d if d < R-r else 0


class UnionFind:
    def __init__(self, n):                      # 初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ

    def find(self, x):              # 親を出力
        if self.parents[x] == x:
            return x
        else:
            p = self.find(self.parents[x])
            self.parents[x] = p
            return p

    def unite(self, x, y):          # ユニオン
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]:
            x , y = y, x    #yを親にする
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        self.parents[x] = y

    def same(self, x, y):       #xとyが同じグループかどうか
        return self.find(x) == self.find(y)


class Kruskal:
    def __init__(self, n:int, edges:list)->None:
        self.n = n
        self.all_edges = edges
        self.weight = None
        self.edges = None
        self.edges_nouse = None
        self.nodes = None

    def build(self)->None:
        self.weight = 0
        self.edges = []
        self.edges_nouse = []
        self.nodes = set([])
        self.all_edges.sort()
        uf = UnionFind(self.n)
        for w, u, v in self.all_edges:
            if uf.same(u, v):
                self.edges_nouse.append((w, u, v))
            else:
                uf.unite(u, v)
                self.weight += w
                self.edges.append((w, u, v))
                self.nodes |= {u, v}

################################

n, m = map(int, input().split())
towers = []
for _ in range(n):
    x, y = map(int, input().split())
    towers.append(([x, y], 0))
circles = []
for _ in range(m):
    x, y, r = map(int, input().split())
    circles.append(([x, y], r))
towers.sort(key=itemgetter(1))

def f(x):
    tc = towers.copy()
    for i in range(m):
        if x >> i & 1:
            tc.append(circles[i])

    edges = []
    for i in range(len(tc)):
        for j in range(i):
            edges.append((distCtoC(tc[i], tc[j]), i, j))

    mst = Kruskal(n+m, edges)
    mst.build()
    return mst.weight

ret = INF
for x in range(1<<m):
    ret = min(ret, f(x))
print(ret)
