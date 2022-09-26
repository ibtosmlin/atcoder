# https://atcoder.jp/contests/abc270/tasks/abc270_f
import sys
sys.setrecursionlimit(10001000)
INF = float('inf')
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, x):
        p = self.parents[x]
        if p == x: return x
        self.parents[x] = p = self.find(p)
        return p

    def unite(self, x, y):
        x = self.find(x); y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]: x , y = y, x
        if self.ranks[x] == self.ranks[y]: self.ranks[y] += 1
        self.parents[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


class Kruskal:
    def __init__(self, n:int, G:list)->None:
        self.n = n
        self.all_edges = G
        self.weight = None
        self.nodes = None

    def build(self)->None:
        self.weight = 0
        self.nodes = set([])
        self.all_edges.sort(key = lambda x: x[-1])
        uf = UnionFind(self.n)
        for u, v, w in self.all_edges:
            if uf.same(u, v):
                continue
            else:
                uf.unite(u, v)
                self.weight += w
                self.nodes |= {u, v}
        if len(self.nodes) != self.n:
            self.weight = INF

################################

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
G = []
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G.append((a, b, w))

def main():

    # A + P + R -----------------------
    Gxyz = G[:]
    for i, xi in enumerate(x):
        Gxyz.append((i, n, xi))
    for i, yi in enumerate(y):
        Gxyz.append((i, n+1, yi))
    m = n + 2
    mst = Kruskal(m, Gxyz)
    mst.build()
    ret_apr = mst.weight

    # A + R -----------------------
    Gxyz = G[:]
    for i, xi in enumerate(x):
        Gxyz.append((i, n, xi))
    m = n + 1
    mst = Kruskal(m, Gxyz)
    mst.build()
    ret_ar = mst.weight

    # P + R -----------------------
    Gxyz = G[:]
    for i, yi in enumerate(y):
        Gxyz.append((i, n, yi))
    m = n + 1
    mst = Kruskal(m, Gxyz)
    mst.build()
    ret_pr = mst.weight

    # R -----------------------
    Gxyz = G[:]
    m = n
    mst = Kruskal(m, Gxyz)
    mst.build()
    ret_r = mst.weight
    print(min(ret_apr, ret_ar, ret_pr, ret_r))

main()