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


# 全方位木DP

class Tree():
    def __init__(self, n, G):
        self.n = n
        self.G = G
        self.root = None            # 根
        self.size = [0] * n         # 部分木のノード数
        self.depth = [-1] * self.n  # 深さ
        self.par = [-1] * self.n    # 親
        self.order = [] # 深さ優先探索の行きがけ順


    def set_root(self, root):
        """DFS
        """
        G = self.G
        self.root = root
        self.depth[root] = 0
        self.order.append(root)
        que = deque([(root, 0)])
        while que:
            x, d = que.pop()
            for nx in G[x]:
                if self.depth[nx] != -1: continue
                self.par[nx] = x
                self.depth[nx] = d + 1
                self.order.append(nx)
                que.append((nx, d + 1))
        for x in self.order[::-1]:
            for nx in G[x]:
                if self.par[x] == nx: continue
                self.size[x] += self.size[nx]
            self.size[x] += 1

    # dpv=g(merge(f(dpc1,c1),f(dpc2,c2),…,f(dpck,ck)),v) (ci∈ch(v))

    def op_before(self, dp_c, c):
        """子供のdpの情報dp_cと子供の情報で処理
        """
        return dp_c + 1

    def merge(self, u, v):
        """処理後の情報でマージ：モノイド
        """
        return u * v % m

    def op_after(self, merge_v, p):
        """マージ後の値と親情報で処理
        """
        return merge_v


    def rerooting(self):
        G = self.G
        op_b = self.op_before
        op_a = self.op_after
        merge = self.merge
        id = 1
        dp = [id] * self.n
        dp2 = [id] * self.n
        left = [id] * self.n
        right = [id] * self.n

        for x in self.order[::-1]:
            px = self.par[x]
            tmp = id
            for nx in G[x]:
                if px == nx: continue
                left[nx] = tmp
                tmp = merge(tmp, op_b(dp[nx], nx))

            tmp = id
            for nx in G[x][::-1]:
                if px == nx: continue
                right[nx] = tmp
                tmp = merge(tmp, op_b(dp[nx], nx))
            dp[x] = op_a(tmp, x)
#        print(dp)

        for x in self.order[1:]:
            px = self.par[x]                    # xの親px
            dp2_x = merge(left[x], right[x])    # 親の自分以外の子供の部分木を集めたもの
            dp2_x = merge(dp2_x, dp2[px])       # 親の親から引き継いだdp2[px]とマージ
            dp2_x = op_b(dp2_x, px)             # 親を子とした時の部分木の値
            dp2[x] = dp2_x
            dp[x] = op_a(merge(dp[x], dp2_x), x)

#        print(dp, left, right, dp2, dp)

        return dp

##########################################################

#n = int(input())
n, m =map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)

T = Tree(n, G)

T.set_root(0)
dp = T.rerooting()
print("\n".join(map(str, dp)))