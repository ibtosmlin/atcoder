# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bo
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
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, x):
        p = self.parents[x]
        if p == x: return x
        self.parents[x] = p = self.find(p)
        return p

    def unite(self, x, y):
        x = self.find(x); y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]: x , y = y, x
        if self.ranks[x] == self.ranks[y]: self.ranks[y] += 1
        self.parents[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


class Kruskal:
    def __init__(self, n:int, G:list)->None:
        self.n = n
        self.all_edges = G
        self.weight = None
        self.edges = None
        self.edges_nouse = None
        self.nodes = None

    def build(self)->None:
        self.weight = 0
        self.edges = []
        self.edges_nouse = []
        self.nodes = set([])
        self.all_edges.sort(key=lambda x: x[-1])
        uf = UnionFind(self.n)
        for u, v, w in self.all_edges:
            if not uf.same(u, v):
                uf.unite(u, v)
                self.weight += w
                # self.edges.append((u, v, w))
                self.nodes |= {u, v}
            else:
                pass
                # self.edges_nouse.append((u, v, w))
        if len(self.nodes) != self.n:
            self.weight = float('inf')
################################

n, m = map(int, input().split())

#辺リストの作成
G = []
for i in range(m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G.append((a, b, w))

mst = Kruskal(n, G)
mst.build()
print(mst.weight)
