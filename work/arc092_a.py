# https://atcoder.jp/contests/abc091/tasks/arc092_a
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

from collections import deque

##二部マッチング

class BipartileMatching:
    ##L2R:Lから見たRのマッチングを記録
    ##R2L:Rから見たLのマッチングを記録
    ##backpath:L側に逆辺が張られている場合の辿る先
    ##root:逆辺を考慮したLの始点を記録

    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.G = [[] for _ in range(L)]
        self.L2R = None
        self.R2L = None

    def add_edge(self, u, v):
        self.G[u].append(v)

    @property
    def matching(self):
        L = self.L
        R = self.R
        L2R = [-1] * L
        R2L = [-1] * R
        backpath = [-1] * L
        root = [-1] * L
        res, f = 0, True
        while f:
            f = False
            q=deque()
            for i in range(L):
                ##まだマッチング対象が見つかっていなければ
                ##iを始点としてキューに追加
                if L2R[i] == -1:
                    root[i] = i
                    q.append(i)

            while q:
                s = q.popleft()
                ##逆辺を辿った先のrootが-1になっていればcontinue
                if ~L2R[root[s]]: continue

                ##始点から接続されている辺を全探索する
                for t in self.G[s]:
                    if R2L[t] == -1:
                        ##逆辺が存在する場合は辿っていく
                        while t != -1:
                            R2L[t] = s
                            L2R[s], t = t , L2R[s]
                            s = backpath[s]
                        f = True
                        res += 1
                        break

                    ##仮のtに対するマッチング候補の情報を更新しキューに追加する
                    temps = R2L[t]
                    if ~backpath[temps]: continue
                    backpath[temps] = s
                    root[temps] = root[s]
                    q.append(temps)

            ##更新があれば逆辺・始点情報を初期化する
            if f:
                backpath = [-1] * L
                root = [-1] * L
        self.L2R = L2R
        self.R2L = R2L
        return res

#################################
n = int(input())
BM = BipartileMatching(n, n)
R = [tuple(map(int, input().split())) for _ in range(n)]
B = [tuple(map(int, input().split())) for _ in range(n)]

for i, (a, b) in enumerate(R):
    for j, (c, d) in enumerate(B):
        if a < c and b < d:
            BM.add_edge(i, j)

print(BM.matching)
