# https://atcoder.jp/contests/typical90/tasks/typical90_an
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from atcoder.maxflow import MFGraph

#############
INF = 10 ** 18
n, w = map(int, input().split())
A = list(map(int, input().split()))
keys=[[] for _ in range(n)]
mf = MFGraph(n+2)
s = n; t = s+1

for i in range(n):
    mf.add_edge(s, i, A[i])
    mf.add_edge(i, t, w)
    x = list(map(int, input().split()))
    if x[0] == 0: continue
    for j in x[1:]:
        j -= 1
        mf.add_edge(j, i, INF)

print(sum(A)-mf.flow(s, t))
