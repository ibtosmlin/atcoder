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


class Tree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = None
        self.edges = [[] for _ in range(n)]
        self.lv = n.bit_length()
        self.depth = [None] * n
        self.distance = [None] * n


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


    def _dfs(self, root):
        q = deque()
        q.append((root, 0, 0))
        seen = [False] * self.n
        self.depth[root] = 0
        self.distance[root] = 0
        seen[root] = True
        lastnode = 0
        while q:
            cur, dep, dist = q.popleft()
            for nxt, nd in self.edges[cur]:
                if seen[nxt]: continue
                q.append((nxt, dep+1, dist+nd))
                self.depth[nxt] = dep+1
                self.distance[nxt] = dist+nd
                seen[nxt] = True
                lastnode = nxt
        return lastnode


    def diameter(self):
        u = self._dfs(0)
        v = self._dfs(u)
        d = self.depth[v]
        return u, v, d

########################################
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
        self._distance = [None] * n
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
        self._distance[self.root] = 0
        self.p[0][self.root] = 0
        while q:
            cur, dep, dist = q.popleft()
            for nxt, nd in self.edges[cur]:
                if self.p[0][nxt]!=None: continue
                q.append((nxt, dep+1, dist+nd))
                self.depth[nxt] = dep+1
                self._distance[nxt] = dist+nd
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
        return self._distance[u] + self._distance[v] - 2 * self._distance[lca]


    def find_kth_parent(self, v, k):
        if not self.is_constructed:
            self.__construct()
        for i in range(self.lv):
            if k & (1 << i):
                v = self.p[i][v]
        return v

n = int(input())
td = Tree(n)
lcu = lca(n)
lcv = lca(n)

for i in range(n-1):
    u, v = map(int1, input().split())
    td.add_edge(u, v)
    lcu.add_edge(u, v)
    lcv.add_edge(u, v)

u, v, d = td.diameter()
lcu.set_root(u)
lcv.set_root(v)

print(u, v)

q = int(input())
for _ in range(q):
    x, di = map(int, input().split())
    x -= 1
    if lcu.nodesdist(u, x) >= di:
        lu = lcu.la(x, di)
        print(lu)
    elif lcv.nodesdist(v, x) >= di:
        lv = lcv.la(x, di)
        print(lv)
    else:
        print(-1)