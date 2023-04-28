#name#
# Graph最小費用流
#description#
# Graph最小費用流
#body#


# 最小費用流問題
# 各辺に容量とコストが設定されたフローネットワークにおいて、
# 始点s から終点t まで流量F のフローを流すための最小コストを求める
# Minimum Cost Flow : O(FElogV)
# ダイクストラ
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_B
from heapq import heappush, heappop
class MinCostFlow:
    def __init__(self, n:int) -> None:
        self.n = n
        self.ln = n.bit_length()
        self.g = [[] for i in range(n)]
        self.INF = float('inf')


    def add_edge(self, fm: int, to: int, cap: int, cost: int):
        # cap: 容量, to/fm:行き先, rev:相方の辺, cost:
        forward = [cap, to, cost, len(self.g[to])]
        backward = [0, fm, -cost, len(self.g[fm])]
        self.g[fm].append(forward)
        self.g[to].append(backward)


    def min_cost_flow(self, s: int, t: int, f: int):
        flow = 0
        prev_v = [-1] * self.n
        prev_e = [-1] * self.n
        while f > 0:
            h = [0] * self.n
            dist = [self.INF]*self.n
            dist[s] = 0
            next_q = []
            heappush(next_q, s)
            while next_q:
                x = heappop(next_q)
                d, v = x >> self.ln, x % (1 << self.ln)
                if dist[v] < d: continue
                for i, (_cap, nv, c, r) in enumerate(self.g[v]):
                    if _cap > 0 and dist[nv] > dist[v] + c + h[v] - h[nv]:
                        dist[nv] = dist[v] + c + h[v] - h[nv]
                        prev_v[nv] = v
                        prev_e[nv] = i
                        heappush(next_q, (dist[nv] << self.ln) + nv)
            if dist[t] == self.INF:
                return -1

            d, v = f, t
            while v != s:
                d = min(d, self.g[prev_v[v]][prev_e[v]][0])
                v = prev_v[v]

            f -= d
            flow += d * dist[t]
            v = t

            while v != s:
                self.g[prev_v[v]][prev_e[v]][0] -= d
                rev = self.g[prev_v[v]][prev_e[v]][3]
                self.g[v][rev][0] += d
                v = prev_v[v]

        return flow


#############
n, m, f = map(int, input().split())
mf = MinCostFlow(n)
for _ in range(m):
    u, v, c, d = map(int, input().split())
    mf.add_edge(u, v, c, d)

print(mf.min_cost_flow(0, n-1, f))

#prefix#
# Lib_G_最小費用流_mincostflow
#end#
