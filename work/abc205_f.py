# https://atcoder.jp/contests/abc205/tasks/abc205_f
from itertools import *
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys; sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i, base='a'): return chr(ord(base) + i%26)    # i=0->'a', i=25->'z'
def alpind(a, base='a'): return ord(a)-ord(base)
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def printyes(ret:bool): print('Yes' if ret else 'No')
def end(r=-1): exit(print(r))

# 最大流問題
# 始点sと終点tが区別された有向グラフ
# 各辺(u,v)には容量c(u,v)が設定されており、超えないフローが流れます。
# 始点sから終点tへの最大流を求める。
#
# Dinic's algorithm
# 幅優先探索で水を流す向きをざっと決める．
# 深さ優先探索で決められた向きで流せる経路を探し，水を流す．
# 流せなくなったら1に戻る.
# O(∣V∣**2・∣E∣)
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_A
from collections import deque
class Dinic:
    def __init__(self, n:int) -> None:
        self.n = n
        self.inf = float('inf')
        self.g = [[] for i in range(n)]
        self.depth = None
        self.progress = None


    def add_edge(self, fm:int, to:int, cap:int):
        # cap: 容量, to/fm:行き先, rev:相方の辺
        forward = [cap, to, len(self.g[to])]
        backward = [0, fm, len(self.g[fm])]
        self.g[fm].append(forward)
        self.g[to].append(backward)

    # sからの最短距離を計算
    def bfs(self, s:int):
        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.g[v]:
                if cap == 0: continue
                if depth[to] >= 0:continue
                depth[to] = depth[v] + 1
                q.append(to)
        self.depth = depth

    # 増加パスをdfsで探す
    def dfs(self, v:int, t:int, flow:int):
        if v == t: return flow
        g_v = self.g[v]
        for i in range(self.progress[v], len(g_v)):
            self.progress[v] = i
            cap, to, rev = g = g_v[i]
            if cap == 0: continue
            if self.depth[v] >= self.depth[to]: continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0: continue
            g[0] -= d
            self.g[to][rev][0] += d
            return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0: return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, self.inf)
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, self.inf)

#############
h, w, n = map(int, input().split())
N = h + w + n * 2 + 2
mf = Dinic(N)

for i in range(1, h+1):
    mf.add_edge(0, i, 1)

for i in range(1, w+1):
    mf.add_edge(h+2*n+i, N-1, 1)

for i in range(n):
    mf.add_edge(h+1+i, h+n+1+i, 1)


for i in range(n):
    r0, c0, r1, c1 = map(lambda x: int(x)-1, input().split())
    for ri in range(r0, r1+1):
        mf.add_edge(1+ri, h+1+i, 1)
    for ci in range(c0, c1+1):
        mf.add_edge(h+n+1+i, h+2*n+1+ci, 1)

print(mf.max_flow(0, N-1))
