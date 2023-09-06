#name#
# 最小費用流
#description#
# 最小費用流を算出するO(FElogV) ダイクストラ
#body#

# 最小費用流問題
# 各辺に容量とコストが設定されたフローネットワークにおいて、
# 始点s から終点t まで流量F のフローを流すための最小コストを求める
# Minimum Cost Flow : O(FElogV) ダイクストラ
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_B
from heapq import heappush, heappop
class MinCostFlow:
    def __init__(self, n:int) -> None:
        self.n = n
        self.ln = n.bit_length()
        self.g = [[] for _ in range(n)]
        self.INF = float('inf')

    def add_edge(self, fm: int, to: int, cap: int, cost: int):
        # to/fm:行き先, cap: 容量, cost:費用  (rev:相方の辺)
        forward = [cap, to, cost, len(self.g[to])]
        backward = [0, fm, -cost, len(self.g[fm])]
        self.g[fm].append(forward); self.g[to].append(backward)

    def min_cost_flow(self, s: int, t: int, f: int):
        # s⇒t       f:フローの大きさ
        flow, prev_v, prev_e = 0, [-1] * self.n, [-1] * self.n
        while f > 0:
            h = [0] * self.n
            dist, que = [self.INF]*self.n, []
            dist[s] = 0; heappush(que, s)
            while que:
                x = heappop(que)
                d, v = x >> self.ln, x % (1 << self.ln)
                if dist[v] < d: continue
                for i, (_cap, nv, c, r) in enumerate(self.g[v]):
                    nd = dist[v] + c + h[v] - h[nv]
                    if _cap > 0 and dist[nv] > nd:
                        dist[nv], prev_v[nv], prev_e[nv]= nd, v, i
                        heappush(que, (dist[nv] << self.ln) + nv)
            if dist[t] == self.INF: return -1
            d, v = f, t
            while v != s:
                d = min(d, self.g[prev_v[v]][prev_e[v]][0])
                v = prev_v[v]
            f, v, flow = f - d, t, flow + d * dist[t]
            while v != s:
                pvv, pev = prev_v[v], prev_e[v]
                self.g[pvv][pev][0] -= d
                self.g[v][self.g[pvv][pev][3]][0] += d
                v = pvv
        return flow


#############
n, m, f = map(int, input().split())
mf = MinCostFlow(n)
for _ in range(m):
    u, v, c, d = map(int, input().split())
    mf.add_edge(u, v, c, d)

print(mf.min_cost_flow(0, n-1, f))

#prefix#
# Lib_GD_最小費用流_mincostflow
#end#