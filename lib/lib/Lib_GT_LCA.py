#name#
# LCA
#description#
# 最小共通祖先
#body#
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

lca = Lca(n, edges, 0)
q = int(input())
for _ in range(q):
    u, v = map(int1, input().split())
    print(lca.distance(u, v))

#prefix#
# lib_GT_最小共通祖先_LCA
#end#
