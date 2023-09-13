# https://atcoder.jp/contests/typical90/tasks/typical90_as
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

INF = 10**20
n, k = map(int, input().split())

p = [tuple(map(int, input().split())) for _ in range(n)]
def d(i, j): return  (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2

dist = [0] * (1<<n)
for s in range(1<<n):
    for i in range(n):
        if s >> i & 1 == 1: continue
        td = 0
        for j in range(n):
            if s >> j & 1 == 0: continue
            td = max(td, d(i,j))
        if dist[s|1<<i] < td:
            dist[s|1<<i] = td


dp = [[INF] * (1<<n) for _ in range(k+1)]
dp[0][0] = 0

all = (1<<n) - 1
for ki in range(k):
    for s in range(1<<n):
        v = dp[ki][s]
        if v == INF: continue
        r = all & ~s
        u = r
        while u:
            nv = max(v, dist[u])
            if nv < dp[ki+1][s|u]: dp[ki+1][s|u] = nv
            u = (u-1) & r

print(dp[k][-1])

