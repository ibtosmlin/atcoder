# https://atcoder.jp/contests/yahoo-procon2019-final/tasks/yahoo_procon2019_final_b
import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])

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
        for q in self.order:
            dp1[q] = fin(dp1[q])

        return dp1


# a, bはdpの値, uは考察している接点親, vは子
# dpをmerge
merge = lambda a, b: max(a, b)
# dpをmerge後にする作業
op = lambda a, u=-1, v=-1: a + 1
# dpをmerge後にする作業
fin = lambda a, u=-1: a
# mergeの単位元
id = 0
#######################################################

n = int(input())
T = Tree(n)
for _ in range(n-1):
    a, b = map(int, input().split())
    T.add_edge(a-1, b-1)

m = int(input())
S = Tree(m)
for _ in range(m-1):
    a, b = map(int, input().split())
    S.add_edge(a-1, b-1)


T.set_root(0)
S.set_root(0)
dpT = T.rerooting(merge, op, fin, id)
dpS = S.rerooting(merge, op, fin, id)

ret = sum(dpT) * m + sum(dpS)*n + n*m
print(ret)
#print(dpT, dpS)