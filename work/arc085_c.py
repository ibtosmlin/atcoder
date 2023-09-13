# https://atcoder.jp/contests/arc085/tasks/arc085_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from atcoder.maxflow import MFGraph
INF = 10**20
N = int(input())
A = list(map(int, input().split()))
mf = MFGraph(N+2)
s = N
t = s + 1
total = 0
for i, ai in enumerate(A):
    if ai > 0:
        mf.add_edge(s, i, ai)
        mf.add_edge(i, t, 0)
        total += ai
    else:
        mf.add_edge(s, i, 0)
        mf.add_edge(i, t, -ai)

for x in range(1, N+1):
    for y in range(2*x, N+1, x):
        mf.add_edge(y-1, x-1, INF)

ret = mf.flow(s, t)

print(total-ret)
for e in mf.edges(): print(e)