# https://atcoder.jp/contests/abc133/tasks/abc133_f
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



from collections import deque
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
        q = deque([r])
        self._depth[r], self._costs[r], self.p[0][r] = 0, 0, r
        while q:
            cur = q.popleft()
            dep = self._depth[cur]
            dis = self._costs[cur]
            for nxt in self.edges[cur]:
                if type(nxt) != int:
                    nxt, cost, _ = nxt
                else:
                    cost = 1
                if self.p[0][nxt] != None: continue
                q.append(nxt)
                self._depth[nxt], self._costs[nxt], self.p[0][nxt] = dep + 1, dis + cost, cur
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


    def jump(self, u, v, i):
        """
        u -> vへのパスのk番目の頂点
        """
        c = self.lca(u, v)
        du = self._depth[u]
        dv = self._depth[v]
        dc = self._depth[c]

        path_len = du - dc + dv - dc
        if path_len < i:
            return -1

        if du - dc >= i:
            return self.la(u, i)

        return self.la(v, path_len - i)

########################################

n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w, c))
    G[b].append((a, w, c))

lca = Lca(n, G, 0)
query = []
need = [set() for _ in range(n)]
for _ in range(q):
    c, w, u, v = map(int, input().split())
    u -= 1; v -= 1
    r = lca.lca(u, v)
    need[u].add(c)
    need[v].add(c)
    need[r].add(c)
    query.append((c, w, u, v, r))

memo = dict()
depth = [0] * n
ccnt = [0] * n
ctot = [0] * n
def dfs(x, p=-1):
    for c in need[x]:
        memo[(x, c)] = (ccnt[c], ctot[c])
    for nx, w, c in G[x]:
        if nx == p: continue
        depth[nx] = depth[x] + w
        ccnt[c] += 1
        ctot[c] += w
        dfs(nx, x)
        ccnt[c] -= 1
        ctot[c] -= w
dfs(0)

def recalc(x, c, w):
    return depth[x] + memo[(x, c)][0] * w - memo[(x, c)][1]

for c, w, u, v, r in query:
    ret = recalc(u, c, w) + recalc(v, c, w) - 2 * recalc(r, c, w)
    print(ret)