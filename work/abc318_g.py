# https://atcoder.jp/contests/abc318/tasks/abc318_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1= lambda x: int(x) - 1


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
        self.g[fm].append(forward); self.g[to].append(backward)

    # sからの最短距離を計算
    def _bfs(self, s:int):
        depth = [-1] * self.n
        depth[s] = 0; que = deque([s])
        while que:
            v = que.popleft()
            for cap, to, _rev in self.g[v]:
                if cap == 0 or depth[to] >= 0: continue
                depth[to] = depth[v] + 1
                que.append(to)
        self.depth = depth

    # 増加パスをdfsで探す
    def _dfs(self, v:int, t:int, flow:int):
        if v == t: return flow
        g_v = self.g[v]
        for i in range(self.progress[v], len(g_v)):
            self.progress[v] = i
            cap, to, rev = g = g_v[i]
            if cap == 0: continue
            if self.depth[v] >= self.depth[to]: continue
            d = self._dfs(to, t, min(flow, cap))
            if d == 0: continue
            g[0] -= d
            self.g[to][rev][0] += d
            return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self._bfs(s)
            if self.depth[t] < 0: return flow
            self.progress = [0] * self.n
            current_flow = self._dfs(s, t, self.inf)
            while current_flow > 0:
                flow += current_flow
                current_flow = self._dfs(s, t, self.inf)
            if flow >= 2: return flow 

#############

n, m = map(int, input().split())
a, s, c = map(int1, input().split())
mf = Dinic(2*n+1)
t = 2*n

mf.add_edge(a+n, t, 1)
mf.add_edge(c+n, t, 1)
for i in range(n):
    mf.add_edge(i, i+n, 1)

for _ in range(m):
    u, v = map(int1, input().split())
    mf.add_edge(u+n, v, 1)
    mf.add_edge(v+n, u, 1)

ret = mf.max_flow(s+n, t) == 2

print('Yes' if ret else 'No')