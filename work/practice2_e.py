# https://atcoder.jp/contests/practice2/tasks/practice2_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1


# 最小費用流問題
# 各辺に容量とコストが設定されたフローネットワークにおいて、
# 始点s から終点t まで流量F のフローを流すための最小コストを求める
# Minimum Cost Flow : O(FElogV) ダイクストラ
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_6_B
from atcoder.mincostflow import MCFGraph

#############
n, k = map(int, input().split())
mf = MCFGraph(n*2+2)
s = 2*n
t = s + 1
MAXA = 10**18
A = [list(map(int, input().split())) for _ in range(n)]

for hi in range(n):
    mf.add_edge(s, hi, k, 0)
for wi in range(n):
    mf.add_edge(n+wi, t, k, 0)
for hi in range(n):
    for wi in range(n):
        mf.add_edge(hi, wi+n, 1, MAXA-A[hi][wi])
mf.add_edge(s, t, n*k, MAXA)

print(MAXA*n*k-mf.flow(s, t, n*k)[1])
G = [['.'] * n for _ in range(n)]
for e in mf.edges():
    if e.flow == 0 or e.cost == 0: continue
    if 0<=e.src <n or n <= e.dst < s:
        u = e.src; v = e.dst-n
        G[u][v] = 'X'

for gi in G:
    print(''.join(gi))