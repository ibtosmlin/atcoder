# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_em
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
        return {i for i in range(self.n) if self.find(i) == root}

    def size(self, x):
        """xのグループの要素数
        """
        return self.sizes[self.find(x)]

    @property
    def roots(self):
        """親の要素一覧
        """
        return {i for i, x in enumerate(self.parents) if i == x}

    @property
    def all_group_members(self):
        """グループのメンバー一覧
        """
        group_members = defaultdict(list)
        for x in range(self.n):
            group_members[self.find(x)].append(x)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.roots)

################

n, m = map(int, input().split())
uf = UnionFind(n)
line = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    line.append((a, b))

q = int(input())
query = []
connect = [True] * m
for _ in range(q):
    que = list(map(int,input().split()))
    query.append(que)
    if que[0] == 1:
        x = que[1] - 1
        connect[x] = False

for i in range(m):
    if connect[i]:
        u, v = line[i]
        uf.unite(u, v)

ret = []
for i in range(q)[::-1]:
    if query[i][0] == 1:
        x = query[i][1] - 1
        u, v = line[x]
        uf.unite(u, v)
    else:
        u, v = query[i][1:]
        if uf.same(u-1, v-1):
            ret.append('Yes')
        else:
            ret.append('No')
print('\n'.join(ret[::-1]))
# https://atcoder.jp/contests/atc001/tasks/unionfind_a
