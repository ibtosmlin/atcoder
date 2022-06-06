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
        if self.parents[x] == x:
            return x
        else:
            p = self.find(self.parents[x])
            self.parents[x] = p
            return p

    def unite(self, x, y):
        """ユニオン
        """
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]:
            x , y = y, x    #yを親にする
        if self.ranks[x] == self.ranks[y]:
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
d = list(map(int, input().split()))

uf = UnionFind(n)
for _ in range(m):
    _a, _b = map(int,input().split())
    _a -= 1; _b -= 1
    uf.unite(_a, _b)
    d[_a] -= 1
    d[_b] -= 1

if sum(d)!=2*(n-m-1):
    end(-1)


gps = []
roots = list(uf.roots)

for x in roots:
    ds = 0
    membs = []
    for y in uf.members(x):
        ds += d[y]
        membs += [y] * d[y]
    gps.append([ds, deque(membs)])
gps.sort(reverse=True)

if len(gps) == 1:
    if gps[0][0] == 0:
        exit()
    else:
        end(-1)

if gps[-1][0] == 0:
    end(-1)

ret = []
dsi, membsi = gps[0]
for i in range(1, len(gps)):
    if dsi == 0: end(-1)
    dsi_, membsi_ = gps[i]
    x = membsi.pop()
    y = membsi_.pop()
    ret.append((x+1, y+1))
    dsi += dsi_
    dsi -= 2
    membsi += membsi_

for ri in ret:
    print(*ri)