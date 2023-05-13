# https://atcoder.jp/contests/arc039/tasks/arc039_d
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

class LowLink():
    def __init__(self, G):
        self.n = len(G)
        self.ord = [None]*self.n    # DFS 行きがけ順
        self.low = [None]*self.n    # lowlink
        self.son = [[] for _ in range(self.n)]  # son[i] := 頂点iの子を格納したlist
        self.back_edge = [[] for _ in range(self.n)] # back_edge[i] := 頂点iから出る後退辺の終点を格納したlist
        self.tps = []                           # 頂点のトポロジカルソート
        self.bridges = []

    def build(self, root=0):
        # DFSでord, son, tpsを求め、lowを初期化
        time = 0 # DFSでの行きがけ順
        stack = [(None, root)] # 直前にいた頂点, 今いる頂点
        while stack:
            pre, now = stack.pop()
            if self.ord[now] is not None: # 後退辺を通ってきた場合
                if self.ord[pre] < self.ord[now]: continue # 後退辺を根側から進んでいた場合は無視
                self.low[pre] = min(self.low[pre], self.ord[now]) # low[pre]をord[now]でchmin
                self.back_edge[pre].append(now)
                continue
            if pre is not None: self.son[pre].append(now)   # 親子関係を記録
            self.tps.append(now)
            self.ord[now] = time
            self.low[now] = self.ord[now] # low[now]をord[now]で初期化
            time += 1
            for next in G[now]:
                if next == pre: continue
                stack.append((now, next))
        for u in reversed(self.tps):# トポソ逆順にlowを求める
            for v in self.son[u]:
                self.low[u] = min(self.low[u], self.low[v])
            for v in self.son[u]:
                if self.low[v] > self.ord[u]:
                    self.bridges.append((min(u, v), max(u, v)))

    def two_edge_connected_component(self):
        # 二重辺連結成分分解
        tecc = []                   # tecc[i] := 連結成分iの頂点グループ
        tecc_idx = [None]*self.n    # tecc_idx[i] := 頂点iが属する連結成分ID
        tecc_tree = []              # 連結成分を頂点、橋を辺としたグラフ(木)の隣接リスト

        sub_roots = [(None, 0)]     # 橋を見つけるごとに、その先は部分木として別にDFSしなおす。
        idx = 0     # 今いる頂点の連結成分の番号
        while sub_roots:
            stack = [sub_roots.pop()] # 部分木の根からDFS
            tecc.append([]) # 今いる頂点の連結成分を格納するlistを追加
            tecc_tree.append([]) # 今いる頂点の連結成分の隣接先を格納するlistを追加
            while stack:
                pre, now = stack.pop()
                tecc[idx].append(now)   # 今いる頂点を連結成分idxに追加
                tecc_idx[now] = idx     # 今いる頂点の連結成分の番号idxを記録
                if pre is not None and idx != tecc_idx[pre]: # 直前に橋を通ってきていたら
                    tecc_tree[idx].append(tecc_idx[pre]) # その橋で繋がれた2つの連結成分を辺で結ぶ
                    tecc_tree[tecc_idx[pre]].append(idx)
                for next in self.son[now]:
                    if self.low[next] > self.ord[now]: # 橋なら
                        sub_roots.append((now, next)) # その先は別の連結成分
                    else:
                        stack.append((now, next)) # その先は同じ連結成分なのでDFSを続ける
            idx += 1
        return tecc, tecc_idx, tecc_tree

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
                    nxt, cost = nxt
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



#########################################
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    w = 0
    G[a].append(b)
    G[b].append(a)

ll = LowLink(G)
ll.build()
tecc, tecc_idx, tecc_tree = ll.two_edge_connected_component()
lca = Lca(len(tecc_tree), tecc_tree, 0)
lca.construct()
q = int(input())
# print(tecc, tecc_idx, tecc_tree)
# print(ll.tps,ll.bridges)
for _ in range(q):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1; c -= 1
    ga, gb, gc = tecc_idx[a], tecc_idx[b], tecc_idx[c]
    if lca.distance(ga, gc) == lca.distance(ga, gb) + lca.distance(gb, gc):
        print('OK')
    else:
        print('NG')

