#name#
# LCA
#description#
# 最小共通祖先
#body#
class Lca():
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
        self._depth = [None] * n
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
        self._depth[self.root] = 0
        self._distance[self.root] = 0
        self.p[0][self.root] = 0
        while q:
            cur, dep, dist = q.popleft()
            for nxt, nd in self.edges[cur]:
                if self.p[0][nxt]!=None: continue
                q.append((nxt, dep+1, dist+nd))
                self._depth[nxt] = dep+1
                self._distance[nxt] = dist+nd
                self.p[0][nxt] = cur
        # ダブリング
        for i in range(1, self.lv):
            for v in range(self.n):
                self.p[i][v] = self.p[i-1][self.p[i-1][v]]
        self.is_constructed = True


    def la(self, x, h):
        if not self.is_constructed: self.__construct()
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
        if not self.is_constructed: self.__construct()
        if self._depth[u] < self._depth[v]: u, v = v, u
        u = self.la(u, self._depth[u] - self._depth[v])
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
        if not self.is_constructed: self.__construct()
        lca = self.lca(u, v)
        return self._depth[u] + self._depth[v] - 2 * self._depth[lca]


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
        if not self.is_constructed: self.__construct()
        lca = self.lca(u, v)
        return self._distance[u] + self._distance[v] - 2 * self._distance[lca]


########################################

n, q = map(int, input().split())
l = lca(n)
l.set_root(0)
for i, ai in enumerate(list(map(int, input().split()))):
    l.add_edge(ai, i+1)


for i in range(q):
    u, v = map(int1, input().split())
    print(l.lca(u, v))

#prefix#
# lib_GT_最小共通祖先_LCA
#end#
