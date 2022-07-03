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
# トポロジカルソート
# 有向非巡回グラフ（DAG）の各ノードを順序付けして、どのノードもその出力辺の先のノードより前にくるように並べることである。
# 有向非巡回グラフは必ずトポロジカルソートすることができる。
class topological_sort:
    def __init__(self, n:int) -> None:
        self.n = n
        self.in_cnt = [0] * n   # 入力
        self.ts = []            # トポロジカルソート
        self.parents = [-1] * n # 親 -1は根
        self.edges = [[] for _ in range(n)] # 辺
        self.node_zero = []     # ゼロ次のノード

    def add_edge(self, fm:int, to:int) -> None:
        self.edges[fm].append(to)
        self.in_cnt[to] += 1

    def _build_sort_by_appear(self) -> None:
        q = self.node_zero[:]
        q = deque(q)
        while q:
            p = q.popleft()
            self.ts.append(p)
            for nxt in self.edges[p]:
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
            for nxt in self.edges[p]:
                self.in_cnt[nxt] -= 1
                if self.in_cnt[nxt] == 0:
                    heappush(q, nxt)
                    self.parents[nxt] = p

    def build(self, sorttype='appear'):
        self.ts = []            # トポロジカルソート
        self.node_zero = [i for i in range(self.n) if self.in_cnt[i] == 0]
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

n = int(input())
m = int(input())
ts = topological_sort(n)
# 隣接リストの作成
for i in range(m):
    # a->b 有向辺
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ts.add_edge(a, b)

ts.build()

fg = True
for i in range(n):
    print(ts.ts[i]+1)
    if i != 0 and not ts.ts[i] in ts.edges[ts.ts[i-1]]:
        fg = False
if fg:
    print(0)
else:
    print(1)
