# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_d
# 全方位tree

from collections import deque

class Tree():
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.root = None    # 根
        self.size = [1] * n # 部分木のノード数
        self.depth = [-1] * self.n
        self.par = [-1] * self.n
        self.order = [] # 深さ優先探索の行きがけ順

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def set_root(self, root):
        self.root = root
        self.depth[root] = 0
        self.order.append(root)
        nxt_q = deque([root])
        while nxt_q:
            p = nxt_q.pop() # 深さ優先探索
            for q in self.edges[p]:
                if self.depth[q] != -1: continue
                self.par[q] = p
                self.depth[q] = self.depth[p] + 1
                self.order.append(q)
                nxt_q.append(q)
        for p in self.order[::-1]:
            for q in self.edges[p]:
                if self.par[p] == q: continue
                self.size[p] += self.size[q]

    def rerooting(self, merge, op, fin, id):
        dp1 = [id] * self.n
        dp2 = [id] * self.n
        for p in self.order[::-1]:
            t = id
            for q in self.edges[p]:
                if self.par[p] == q: continue
                dp2[q] = t
                t = merge(t, op(dp1[q], p, q))
            t = id
            for q in self.edges[p][::-1]:
                if self.par[p] == q: continue
                dp2[q] = merge(t, dp2[q])
                t = merge(t, op(dp1[q], p, q))
            dp1[p] = t
        for q in self.order[1:]:
            pq = self.par[q]
            dp2[q] = op(merge(dp2[q], dp2[pq]), q, pq)
            dp1[q] = merge(dp1[q], dp2[q])
        return dp1


n, m = map(int, input().split())
T = Tree(n)


#######################################################
# a, bはdpの値, uは考察している接点親, vは子
# dpをmerge
merge = lambda a, b: a * b % m
# dpをmerge前にする作業
op = lambda a, u, v: a + 1
# dpをmerge後にする作業
fin = lambda a, u: a
# mergeの単位元
id = 1
#######################################################

for _ in range(n-1):
    a, b = map(int, input().split())
    T.add_edge(a-1, b-1)

T.set_root(0)
dp = T.rerooting(merge, op, fin, id)
ret = dp
print("\n".join(map(str, ret)))
