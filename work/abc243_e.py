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
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'

#name#
# 最小全域木
#description#
# 最小全域木 クラスカル法 minimum_spanning_tree
# 重み付き無向グラフで、それらの全ての頂点を結び連結するような木の最小のコストを求める
# 辺の重みの小さい順にみて、連結成分が閉路にならない辺を追加していく
# つなぐ頂点が同じ連結成分にないことをUnion Find Tree でみる
#body#

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
        self.edges = []
        self.dist = [[INF]*n for _ in range(n)]

    def add(self, u, v, w):
        fg = False
        for i in range(self.n):
            if i == u or i == v:
                continue

        self.weight += 1
        self.dist[u][v] = w
        self.dist[v][u] = w
        self.edges.append((u, v, w))


    def build(self)->None:
        self.weight = 0
        self.all_edges.sort()
        uf = UnionFind(self.n)
        for w, u, v in self.all_edges:
            for i in range(self.n):
                if self.dist[u][i] > w + self.dist[v][i]:


################################

n, m = map(int, input().split())

#辺リストの作成
edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((w, a-1, b-1))

mst = Kruskal(n, edges)
mst.build()
print(m-mst.weight)
print(mst.edges)

#prefix#
# Lib_最小全域木_MST
#end#