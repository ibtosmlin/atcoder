#name#
# 最小全域木
#description#
# 最小全域木 クラスカル法 minimum_spanning_tree
# 重み付き無向グラフで、それらの全ての頂点を結び連結するような木の最小のコストを求める
# 辺の重みの小さい順にみて、連結成分が閉路にならない辺を追加していく
# つなぐ頂点が同じ連結成分にないことをUnion Find Tree でみる
#body#
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
        self.edges = None
        self.edges_nouse = None
        self.nodes = None

    def build(self)->None:
        self.weight = 0
        self.edges = []
        self.edges_nouse = []
        self.nodes = set([])
        self.all_edges.sort(key=lambda x: x[-1])
        uf = UnionFind(self.n)
        for u, v, w in self.all_edges:
            if not uf.same(u, v):
                uf.unite(u, v)
                self.weight += w
                # self.edges.append((u, v, w))
                self.nodes |= {u, v}
            else:
                pass
                # self.edges_nouse.append((u, v, w))
        if len(self.nodes) == self.n:
            self.weight = float('inf')
################################

n, m = map(int, input().split())

#辺リストの作成
G = []
for i in range(m):
    a, b, w = map(int1, input().split())
    G.append((a, b, w))

mst = Kruskal(n, G)
mst.build()
print(mst.weight)

#prefix#
# Lib_GT_最小全域木_MST
#end#
