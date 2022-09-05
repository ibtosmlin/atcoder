#name#
# Diameter
#description#
# 木の直径
#body#
class Tree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = None
        self.edges = [[] for _ in range(n)]
        self.lv = n.bit_length()
        self._depth = [None] * n
        self._distance = [None] * n


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
        self._depth[root] = 0
        self._distance[root] = 0
        seen[root] = True
        lastnode = 0
        while q:
            cur, dep, dist = q.popleft()
            for nxt, nd in self.edges[cur]:
                if seen[nxt]: continue
                q.append((nxt, dep + 1, dist + nd))
                self._depth[nxt] = dep + 1
                self._distance[nxt] = dist + nd
                seen[nxt] = True
                lastnode = nxt
        return lastnode


    def diameter(self):
        u = self._dfs(0)
        v = self._dfs(u)
        depth = self._depth[v]
        distance = self._distance[v]
        return u, v, depth, distance


########################################

n = int(input())
td = Tree(n)

for i in range(n-1):
    u, v = map(int1, input().split())
    td.add_edge(u, v)

print(td.edges)
u, v, d = td.diameter()
print(u, v, d)

#prefix#
# lib_GT_木の直径
#end#
