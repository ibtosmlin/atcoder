# https://atcoder.jp/contests/arc030/tasks/arc030_3
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from atcoder.scc import SCCGraph
####################################
class SCC(SCCGraph):
    def __init__(self, n):
        self.N = n
        super().__init__(n)
        self.G = [[] for _ in range(n)]
        self.isbuild = False
        self.group_num = None
        self.ids = None

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self.G[from_vertex].append(to_vertex)
        return super().add_edge(from_vertex, to_vertex)

    def build(self):
        gn, ids = self._internal.scc_ids()
        counts = [0] * gn
        for x in ids: counts[x] += 1
        groups = [[] for _ in range(gn)]
        for v in range(self.N): groups[ids[v]].append(v)
        self.groups = groups
        G0 = [[] for i in range(gn)]
        GP = [[] for i in range(gn)]
        for v in range(self.N):
            lbs = ids[v]
            for w in self.G[v]:
                lbt = ids[w]
                if lbs == lbt: continue
                G0[lbs].append(lbt)
            GP[lbs].append(v)
        self.SG = G0
        self.SGVertex = GP
        return True

    def scc(self):
        if not self.isbuild: self.isbuild = self.build()
        return self.groups

    def dag(self):
        if not self.isbuild: self.isbuild = self.build()
        return self.SG, self.SGVertex


n, m, k = map(int, input().split())
A = list(input().split())

scc = SCC(n)

for i in range(m):
    _a, _b = map(int1, input().split())
    scc.add_edge(_a, _b)

G, LA = scc.dag()
for li in LA:
    for i in range(len(li)):
        li[i] = A[li[i]]
N = len(G)
RG = [[N] for _ in range(N)]
for i in range(N):
    for ni in G[i]:
        RG[ni].append(i)

INF = [10**18]

dp = [[None] * (k+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = ""


for i in range(N):
    for j in RG[i]:
        for l in range(len(LA[i])):
            add = ''.join(LA[i][:l+1])
            for ki in range(k):
                if dp[j][ki] == None: continue
                to = l + ki + 1
                v = dp[j][ki] + add
                if to > k: break
                if dp[i][to] == None:
                    dp[i][to] = v
                else:
                    dp[i][to] = min(v, dp[i][to])

ret = 'z' * 500
for i in range(N):
    if dp[i][k] != None:
        ret = min(ret, dp[i][k])
if ret == 'z' * 500:
    print(-1)
else:
    print(ret)