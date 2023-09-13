# https://atcoder.jp/contests/arc074/tasks/arc074_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
from atcoder.maxflow import MFGraph

INF = 10 ** 20
h, w = map(int, input().split())
A = [input() for _ in range(h)]
s = None
t = None
mf = MFGraph(h*w+h+w)

for i in range(h):
    r = h*w + i
    for j in range(w):
        c = h*w + h + j
        rc = i*w + j
        if A[i][j] == 'S':
            s = rc
            mf.add_edge(s, r, INF)
            mf.add_edge(s, c, INF)
        elif A[i][j] == 'T':
            t = rc
            mf.add_edge(r, t, INF)
            mf.add_edge(c, t, INF)
        elif A[i][j] == 'o':
            mf.add_edge(rc, r, 1)
            mf.add_edge(rc, c, 1)
            mf.add_edge(r, rc, 1)
            mf.add_edge(c, rc, 1)

if s%w == t%w or s//w == t//w:
    print(-1)
    exit()


ret = mf.flow(s, t)
print(-1 if ret == INF else ret)

