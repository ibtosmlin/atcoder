# https://atcoder.jp/contests/abc304/tasks/abc304_e
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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()

class UnionFind:
    def __init__(self, n):                      # 初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.group_count = n                    # グループの数


    def find(self, x):
        """親を出力
        Parameters
        ----------
        x : int
            ノード番号
        """
        if self.parents[x] == x: return x
        self.parents[x] = p = self.find(self.parents[x])
        return p

    def unite(self, x, y):
        """ユニオン
        """
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]:
            x , y = y, x    #yを親にする
        elif self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        self.parents[x] = y
        self.sizes[y] += self.sizes[x]
        self.group_count -= 1

    def same(self, x, y) -> bool:
        """xとyが同じグループかどうか
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """xと同じグループの要素
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def size(self, x):
        """xのグループの要素数
        """
        return self.sizes[self.find(x)]

    def get_roots(self):
        """親のリスト取得
           親ごとのグループのメンバー一覧取得
        """
        _dum = [[] for _ in range(self.n)]
        self.roots = []
        self.group_members = dict()
        for x in range(self.n):
            r = self.find(x)
            if r == x:
                self.roots.append(r)
            _dum[r].append(x)
        for r in self.roots:
            self.group_members[r] = _dum[r]


    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.roots)

################

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int,input().split())
    a -= 1; b -= 1
    uf.unite(a, b)

k = int(input())
cond = defaultdict(set)

memo = dict()
def pa(x):
    if x in memo:
        return memo[x]
    else:
        return uf.find(x)

for _ in range(k):
    a, b = map(int,input().split())
    a -= 1; b -= 1
    a = pa(a)
    b = pa(b)
    if a>b:
        a, b = b, a
    cond[a].add(b)


q = int(input())
for _ in range(q):
    a, b = map(int,input().split())
    a -= 1; b -= 1
    a = pa(a)
    b = pa(b)
    if a > b:
        a, b = b, a
    if b in cond[a]:
        print('No')
    else:
        print('Yes')

