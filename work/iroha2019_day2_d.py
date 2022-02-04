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
        for w, u, v, i in self.all_edges:
            if uf.same(u, v):
                self.edges_nouse.append((w, u, v, i))
            else:
                uf.unite(u, v)
                self.weight += w
                self.edges.append((w, u, v, i))
                self.nodes |= {u, v}

################################

n, m = map(int, input().split())

#辺リストの作成
edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((-w, a-1, b-1, i+1))

mst = Kruskal(n, edges)
mst.build()
mst.edges.sort(key=itemgetter(3))
for _w, _u, _v, i in mst.edges:
    print(i)
