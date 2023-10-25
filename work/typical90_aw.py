# https://atcoder.jp/contests/typical90/tasks/typical90_aw
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

class UnionFind:
    def __init__(self, n):
        self.n, self.parents, self.ranks = n, [i for i in range(n)], [0] * n
    def find(self, x):
        p = self.parents[x]
        if p == x: return x
        self.parents[x] = p = self.find(p); return p
    def unite(self, x, y):
        x = self.find(x); y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]: x , y = y, x
        if self.ranks[x] == self.ranks[y]: self.ranks[y] += 1
        self.parents[x] = y
    def same(self, x, y): return self.find(x) == self.find(y)


class Kruskal:
    def __init__(self, n:int, G:list)->None:
        self.n = n
        self.all_edges = G
        self.edges = [False] * len(G)
        self.weight = 0
        self.nodes = set([])
        self.INF = 10**20
        self.build()

    def build(self)->None:
        uf = UnionFind(self.n)
        for u, v, w, i in sorted([(a, b, w, i) for i, (a, b, w) in enumerate(self.all_edges)], key=lambda x: x[2]):
            if not uf.same(u, v):
                uf.unite(u, v)
                self.weight += w
                self.nodes |= {u, v}
                self.edges[i] = True

        if sum(self.edges) != self.n - 1:
            self.weight = self.INF


n, m = map(int, input().split())

#辺リストの作成
G = []
for i in range(m):
    w, a, b = map(int, input().split())
    a -= 1
    G.append((a, b, w))

mst = Kruskal(n+1, G)
ret = mst.weight
print(-1 if ret == mst.INF else ret)