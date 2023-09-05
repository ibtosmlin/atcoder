# https://atcoder.jp/contests/abc318/tasks/abc318_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1


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


n = int(input())
D = [[0]*n for _ in range(n)]
for i in range(n-1):
    di = list(map(int, input().split()))
    for j in range(n-1-i):
        D[i][1+j+i] = di[j]

mm = MinCostFlow(n*2+2)
s = 2*n
t = 2*n+1

for i in range(n):
    mm.add_edge(s, i, 1, 0)
for i in range(n):
    mm.add_edge(i+n, t, 1, 0)

INF = 10**10
for i in range(n):
    for j in range(i+1, n):
        mm.add_edge(i, j+n, 1, -D[i][j])

print(-mm.min_cost_flow(s, t, n))


