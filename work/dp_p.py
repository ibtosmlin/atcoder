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
class topological_sort:
    def __init__(self, n:int, G) -> None:
        self.n = n
        self.ts = []            # トポロジカルソート
        self.parents = [-1] * n # 親 -1は根
        self.G = G              # 辺
        self.in_cnt = [0] * n   # 入力
        self.node_zero = []     # ゼロ次のノード
        for i, gi in enumerate(G):
            for j, w in gi:
                self.in_cnt[j] += 1
        self.node_zero = [i for i in range(self.n) if self.in_cnt[i] == 0]


    def _build_sort_by_appear(self) -> None:
        q = self.node_zero[:]
        q = deque(q)
        while q:
            p = q.popleft()
            print(p)
            self.ts.append(p)
            for nxt, nxtw in self.G[p]:
                self.in_cnt[nxt] -= 1
                if self.in_cnt[nxt] == 0:
                    q.append(nxt)
                    self.parents[nxt] = p


    def _build_sort_by_nodeid(self) -> None:
        q = self.node_zero[:]
        heapify(q)
        while q:
            p = heappop(q)
            self.ts.append(p)
            for nxt, nxtw in self.G[p]:
                self.in_cnt[nxt] -= 1
                if self.in_cnt[nxt] == 0:
                    heappush(q, nxt)
                    self.parents[nxt] = p


    def build(self, sorttype='appear'):
        self.ts = []            # トポロジカルソート
        if sorttype == 'appear':        # 出たとこ順番
            self._build_sort_by_appear()
        elif sorttype == 'nodeid':      # ノードの順番
            self._build_sort_by_nodeid()

    @property
    def is_dag(self) -> bool:
        return len(self.ts)==self.n
        # True 閉路なしDAG
        # False 閉路あり


#########################################
from collections import deque
# n, m = map(int, input().split())
n = int(input())
G = [[] for _ in range(n)]
m = n-1
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    w = 0
    G[a].append((b, w))
    if a != 0:
        G[b].append((a, w))

ts = topological_sort(n, G)
print(G)
print(ts.node_zero, "x")
print(ts.in_cnt, "y")
ts.build()

print(ts.ts)
print(ts.parents)
print(ts.is_dag)

#prefix#
# Lib_G_トポロジカルソート_topologicalsort
#end#