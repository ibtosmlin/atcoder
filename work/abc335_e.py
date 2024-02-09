
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

from atcoder.scc import SCCGraph as _SCCG

class SCCGraph(_SCCG):
    def __init__(self, n):
        super().__init__(n)
        self.n = None
        self.ids = None
        self.groups = None
        self.G = None

    def scc(self):
        n, ids = self._internal.scc_ids()
        groups = [[] for _ in range(n)]
        for i in range(self._internal._n):
            groups[ids[i]].append(i)
        self.n = n
        self.ids = ids
        self.groups = groups
        return n, ids, groups

    def dag(self):
        self.G = [set() for _ in range(self.n)]
        for fm, to in self._internal._edges:
            fm = self.ids[fm]; to = self.ids[to]
            if fm != to:
                self.G[fm].add(to)
        return self.G

n, m = map(int, input().split())
A = list(map(int, input().split()))
scc = SCCGraph(n)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if A[a] <= A[b]:
        scc.add_edge(a, b)
    if A[a] >= A[b]:
        scc.add_edge(b, a)

scc.scc()
scc.dag()

dp = [0] * scc.n
dp[scc.ids[0]] = 1

for i in range(scc.n):
    if dp[i] == 0: continue
    for j in scc.G[i]:
        dp[j] = max(dp[j], dp[i] + 1)


print(dp[scc.ids[n-1]])

# print(scc.scc_node_count)
# print(scc.scc_node_map)
# print(scc.scc_groups)
# print(scc.scc_G)
# print(dp)