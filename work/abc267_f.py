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


def tree_diameter(n, G):
    root = None
    lv = n.bit_length()
    _depth = [None] * n

    def _dfs(root):
        _depth = [None] * n
        q = deque()
        q.append(root)
        _depth[root] = 0
        last_node = 0
        while q:
            cur = q.popleft()
            dep = _depth[cur]
            for nxt in G[cur]:
                if type(nxt) != int: nxt, _cost = nxt
                if _depth[nxt] != None: continue
                q.append(nxt)
                _depth[nxt] = dep + 1
                last_node = nxt
        return last_node, _depth

    u, _ = _dfs(n-1)
    v, depth = _dfs(u)
    return u, v, depth

##############################

class Lca:
    """Lowest Common Ancestor

    u, vの共通の親
    ダブリング p[i][v] = vの2^i個 親

    Parameters
    ----------
    n : int
        nodeの数
    G : graph
    r : root
    """
    def __init__(self, n: int, G, r:int) -> None:
        self.n = n
        self.root = r
        self.edges = G
        self.lv = n.bit_length()
        self.p = [[None] * n for _ in range(self.lv)]
        self._depth = [None] * n
        self._costs = [None] * n
        self.construct()

    def construct(self):
        """深さと親の設定とダブリング
        """
        # 深さと親の設定
        r = self.root
        q = deque()
        q.append(r)
        self._depth[r] = 0
        self._costs[r] = 0
        self.p[0][r] = r
        while q:
            cur = q.popleft()
            dep = self._depth[cur]
            dis = self._costs[cur]
            for nxt in self.edges[cur]:
                if type(nxt) != int:
                    nxt, cost = nxt
                else:
                    cost = 1
                if self.p[0][nxt] != None: continue
                q.append(nxt)
                self._depth[nxt] = dep + 1
                self._costs[nxt] = dis + cost
                self.p[0][nxt] = cur
        # ダブリング
        for i in range(1, self.lv):
            for v in range(self.n):
                self.p[i][v] = self.p[i-1][self.p[i-1][v]]


    def la(self, x, h):
        """h代前祖先

        """
        for i in range(self.lv)[::-1]:
            if h >= 1 << i:
                x = self.p[i][x]
                h -= 1 << i
        return x


    def lca(self, u, v):
        """共通祖先

        Parameters
        ----------
        u, v : node
            ノード

        Returns
        -------
        int
            共通祖先のノード
        """
        # u,vの高さを合わせる
        if self._depth[u] < self._depth[v]: u, v = v, u
        u = self.la(u, self._depth[u] - self._depth[v])
        if u == v: return u
        # u, vのギリギリ合わない高さまで昇る
        for i in range(self.lv)[::-1]:
            if self.p[i][u] != self.p[i][v]:
                u = self.p[i][u]
                v = self.p[i][v]
        return self.p[0][u]


    def distance(self, u, v):
        lca = self.lca(u, v)
        return self._depth[u] + self._depth[v] - 2 * self._depth[lca]


    def cost(self, u, v):
        lca = self.lca(u, v)
        return self._costs[u] + self._costs[v] - 2 * self._costs[lca]


########################################


n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

u, v, _ = tree_diameter(n, edges)
lcu = Lca(n, edges, u)
lcv = Lca(n, edges, v)

q = int(input())
for _ in range(q):
    x, k = map(int, input().split())
    x -= 1
    if lcu.distance(u, x) >= k:
        print(lcu.la(x, k) + 1)
    elif lcv.distance(v, x) >= k:
        print(lcv.la(x, k) + 1)
    else:
        print(-1)
