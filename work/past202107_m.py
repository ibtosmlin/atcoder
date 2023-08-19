

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
n, c = map(int, input().split())
A = list(map(int, input().split()))
mf = MinCostFlow(n*2+2)
st = 2*n
gl = 2*n + 1

for u in range(n):
    mf.add_edge(st, u, 1, 0)
    mf.add_edge(u, gl, 1, c)

for u in range(n):
    for v in range(u+1, n):
        mf.add_edge(u, v+n, 1, abs(A[u]-A[v]))

for u in range(n):
    mf.add_edge(u+n, gl, 1, 0)



print(mf.min_cost_flow(st, gl, n))
