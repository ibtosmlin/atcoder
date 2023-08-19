# https://atcoder.jp/contests/past202104-open/tasks/past202104_o
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
from collections import defaultdict
import copy

class warshall_floyd:
    def __init__(self, n:int) -> None:
        self.INF = float("inf")
        self.n = n
        self.d = [[self.INF] * n for _ in range(n)]
        #d[u][v] : 辺uvのコスト(存在しないときはinf)
        for i in range(n):
            self.d[i][i] = 0 #自身のところに行くコストは０

    def build(self):
        n = self.n
        wf = copy.deepcopy(self.d)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])

        self.wf = wf #wf[i][j]に頂点i, j間の最短距離を格納

    def add_edge(self, fm, to, cost):
        self.d[fm][to] = cost


    # 負値閉路検索
    @property
    def is_neg_cycle(self) -> bool:
        for i in range(self.n):
            if self.wf[i][i] < 0:
                return True
        return False


    # 経路復元
    def path(self, s, g):
        ret = []
        if s == g or self.wf[s][g] == self.INF:
            return ret
        cur = s
        while cur!=g:
            for nxt in range(self.n):
                if nxt==cur or nxt==s: continue
                if self.d[cur][nxt] + self.wf[nxt][g] == self.wf[cur][g]:
                    ret.append((cur, nxt))
    #                ret.append((nxt, cur))
                    cur = nxt
                    break
        return ret

##############################
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
        self.memodist = defaultdict(int)
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
        if not (u, v) in self.memodist:
            lca = self.lca(u, v)
            self.memodist[(u, v)] = self._depth[u] + self._depth[v] - 2 * self._depth[lca]
        return self.memodist[(u, v)]

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

from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n)]
edges = []
for i in range(m):
    a, b = map(int1, input().split())
    G[a].append((b, i))
    G[b].append((a, i))
    edges.append((a, b))

used = set()

seen = [False] * n
que = deque([])
seen[0] = True
que.append(0)
while que:
    x = que.popleft()
    for nx, i in G[x]:
        if seen[nx]: continue
        seen[nx] = True
        que.append(nx)
        used.add(i)

G = [[] for _ in range(n)]
for i in range(m):
    if i in used:
        a, b = edges[i]
        G[a].append(b)
        G[b].append(a)

lca = Lca(n, G, 0)

extnodes = set()
for i in range(m):
    if not i in used:
        a, b = edges[i]
        extnodes.add(a)
        extnodes.add(b)

extpos = {v:i for i, v in enumerate(sorted(extnodes))}
en = len(extpos)

WF = warshall_floyd(en)

for x in extnodes:
    xp = extpos[x]
    for y in extnodes:
        yp = extpos[y]
        WF.add_edge(xp, yp, lca.distance(x, y))

for i in range(m):
    if not i in used:
        a, b = edges[i]
        ap = extpos[a]
        bp = extpos[b]
        WF.add_edge(ap, bp, 1)
        WF.add_edge(bp, ap, 1)

WF.build()

q = int(input())
for _ in range(q):
    u, v = map(lambda x: int(x)-1, input().split())
    ret = lca.distance(u, v)
    for x in extnodes:
        xp = extpos[x]
        for y in extnodes:
            yp = extpos[y]
            ret = min(ret, lca.distance(u, x) + WF.wf[xp][yp] + lca.distance(y, v))
    print(ret)

