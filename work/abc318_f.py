# https://atcoder.jp/contests/abc318/tasks/abc318_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1


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
n = int(input())
x = list(map(int, input().split()))
l = list(map(int, input().split()))

def isok(k):
    mf = Dinic(2*n+2)
    s = 2*n
    t = 2*n+1
    for i in range(n):
        for j in range(n):
            if k - l[i] <= x[i] <= k + l[i]:
                mf.add_edge(i, n+i, 1)
    for i in range(n):
        mf.add_edge(s, i, 1)
    for i in range(n):
        mf.add_edge(n+i, t, 1)
    return n == mf.max_flow(s, t)

fg = False
for i in range(n):
    if not isok(x[i]): continue
    fg = True
    u = x[i]

# if fg == False: exit(print(0))

ng = -10**20
ok = u
while ok - ng > 1:
    mid = (ok+ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid

okl = ok


ng = 10**20
ok = u
while ng - ok > 1:
    mid = (ok+ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid

oku = ok


print(oku-okl+1)
if n == 3:
    ret = 0
    for i in range(-1000, 1000):
        if isok(i):
            ret += 1
    print(ret)