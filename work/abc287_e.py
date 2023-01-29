# https://atcoder.jp/contests/abc287/tasks/abc287_e
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
class UnionFindWeighted:
    def __init__(self, n):                      # 初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.weights = [0] * n                  # 親との重み
        self.isvalid = [True] * n               # ポテンシャルがプラスの閉路あり

    #親を出力
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            p = self.find(self.parents[x])
            self.weights[x] += self.weights[self.parents[x]]
            self.parents[x] = p
            return p

    # ユニオン
    def unite(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            if self.diff(x, y) != w:
                self.isvalid[rx] = False
                return "invalid"
            else:
                return "pass"
        # a[x]->a[y]  の差はw  # a[y] = a[x] + w
        wx = self.weight(x)
        wy = self.weight(y)
        if rx == ry: return
        if self.ranks[rx] > self.ranks[ry]:
            rx , ry = ry, rx    #ryを親にする
            wx , wy = wy, wx
            w *= -1
        self.parents[rx] = ry
        self.sizes[ry] += self.sizes[rx]
        self.weights[rx] = wy - wx - w
        if self.ranks[rx]==self.ranks[ry]:
            self.ranks[rx] += 1
        self.isvalid[ry] &= self.isvalid[rx]
        return "unite"

    #xとyが同じグループかどうか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #xと同じグループの要素
    def members(self, x):
        root = self.find(x)
        return {i for i in range(self.n) if self.find(i) == root}

    #グループの要素数
    def size(self, x):
        root = self.find(x)
        return self.sizes[root]

    #親の要素一覧
    def roots(self):
        return {i for i, x in enumerate(self.parents) if i == x}

    #グループの個数
    def group_count(self):
        return len(self.roots())

    #グループのメンバー一覧
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    #重みの差
    def weight(self, x):
        _ = self.find(x)
        return self.weights[x]

    #重み
    def diff(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry: return float('inf')
        return self.weight(y) - self.weight(x)

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

################

n = int(input())
uf = UnionFindWeighted(n+26)

for i, ai in enumerate(alp):
    for j, aj in enumerate(alp):
        if ai == aj: continue
        if i > j: continue
        uf.unite(ai, aj, 0)


for _ in range(n):
    a, b, w = map(int,input().split())
    a -= 1; b -= 1
    uf.unite(a, b, w)
