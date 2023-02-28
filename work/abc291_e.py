# https://atcoder.jp/contests/abc291/tasks/abc291_e
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


# https://atcoder.jp/contests/atc001/tasks/unionfind_a

# トポロジカルソート
# 有向非巡回グラフ（DAG）の各ノードを順序付けして、どのノードもその出力辺の先のノードより前にくるように並べることである。
# 有向非巡回グラフは必ずトポロジカルソートすることができる。
class topological_sort:
    def __init__(self, n:int, G) -> None:
        self.n = n
        self.ts = []            # トポロジカルソート
        self.parents = [-1] * n # 親 -1は根
        self.G = G              # 辺
        self.in_cnt = [0] * n   # 入力
        self.node_zero = []     # ゼロ次のノード
        for i, gi in enumerate(G):
            for j in gi:
                self.in_cnt[j] += 1
        self.node_zero = [i for i in range(self.n) if self.in_cnt[i] == 0]


    def _build_sort_by_appear(self) -> None:
        q = self.node_zero[:]
        q = deque(q)
        while q:
            p = q.popleft()
            self.ts.append(p)
            for nxt in self.G[p]:
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


    @property
    def is_unique(self) -> bool:
        if not self.is_dag: return False
        for i in range(self.n-1):
            u, v = self.ts[i:i+2]
            if not v in self.G[u]: return False
        return True
        # True トポロジカルソートの経路が一意
        # False 複数あり

#########################################
from collections import deque
n, m = map(int, input().split())


G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    w = 0
    G[a].append(b)

ts = topological_sort(n, G)
ts.build()
if not ts.is_unique: end('No')

print('Yes')
ret = [0] * n
for i, u in enumerate(ts.ts):
    ret[u] = i+1
print(*ret)
