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
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()
from collections import deque


class lca():
    """Lowest Common Ancestor

    u, vの共通の親
    ダブリング p[i][v] = vの2^i個 親

    Parameters
    ----------
    n : int
        nodeの数

    Methods
    ----------
    set_root :



    """
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = None
        self.edges = [[] for _ in range(n)]
        self.lv = n.bit_length()
        self.p = [[None] * n for _ in range(self.lv)]
        self.depth = [None] * n
        self.distance = [None] * n
        self.is_constructed = False


    def set_root(self, root: int = 0) -> None:
        """木の根を設定する

        Parameters
        ----------
        root : int
            省略時は 0
        """
        self.root = root
        self.is_constructed = False


    def add_edge(self, fm: int, to: int, dist: int=1) -> None:
        """辺の設定

        Parameters
        ----------
        fm : int
            辺の始点
        to : [type]
            辺の終点
        """
        self.edges[fm].append((to, dist))
        self.is_constructed = False


    def __construct(self):
        """深さと親の設定とダブリング
        """
        # 深さと親の設定
        q = deque()
        q.append((self.root, 0, 0))
        self.depth[self.root] = 0
        self.distance[self.root] = 0
        self.p[0][self.root] = 0
        while q:
            cur, dep, dist = q.popleft()
            for nxt, nd in self.edges[cur]:
                if self.p[0][nxt]!=None: continue
                q.append((nxt, dep+1, dist+nd))
                self.depth[nxt] = dep+1
                self.distance[nxt] = dist+nd
                self.p[0][nxt] = cur
        # ダブリング
        for i in range(1, self.lv):
            for v in range(self.n):
                self.p[i][v] = self.p[i-1][self.p[i-1][v]]
        self.is_constructed = True


    def la(self, x, h):
        if not self.is_constructed:
            self.__construct()
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
        if not self.is_constructed:
            self.__construct()
        if self.depth[u] < self.depth[v]: u, v = v, u
        u = self.la(u, self.depth[u] - self.depth[v])
        if u == v: return u
        # u, vのギリギリ合わない高さまで昇る
        for i in range(self.lv)[::-1]:
            if self.p[i][u] != self.p[i][v]:
                u = self.p[i][u]
                v = self.p[i][v]
        return self.p[0][u]


    def nodesdist(self, u, v):
        """ノード間の距離

        Parameters
        ----------
        u, v : node
            ノード

        Returns
        -------
        int
            ノード間の距離
        """
        if not self.is_constructed:
            self.__construct()
        lca = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca]


    def distance(self, u, v):
        """ノード間の経路の長さ

        Parameters
        ----------
        u, v : node
            ノード

        Returns
        -------
        int
            ノード間の距離
        """
        if not self.is_constructed:
            self.__construct()
        lca = self.lca(u, v)
        return self.distance[u] + self.distance[v] - 2 * self.distance[lca]


########################################

n = int(input())
l = lca(n)

for i in range(n):
    p = int(input())
    if p == -1:
        l.set_root(i)
    else:
        p -= 1
        l.add_edge(p, i, 1)
q = int(input())
for i in range(q):
    u, v = map(int1, input().split())
    la = l.lca(u, v)
    if la == v:
        print('Yes')
    else:
        print('No')
