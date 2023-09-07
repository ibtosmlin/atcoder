# https://atcoder.jp/contests/abc318/tasks/abc318_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1= lambda x: int(x) - 1

from atcoder.maxflow import MFGraph
#############

n, m = map(int, input().split())
a, s, c = map(int1, input().split())
mf = MFGraph(2*n+1)
t = 2*n

mf.add_edge(a+n, t, 1)
mf.add_edge(c+n, t, 1)
for i in range(n):
    mf.add_edge(i, i+n, 1)

for _ in range(m):
    u, v = map(int1, input().split())
    mf.add_edge(u+n, v, 1)
    mf.add_edge(v+n, u, 1)

ret = mf.flow(s+n, t) == 2

print('Yes' if ret else 'No')