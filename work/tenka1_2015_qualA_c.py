# https://atcoder.jp/contests/tenka1-2015-quala/tasks/tenka1_2015_qualA_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from atcoder.maxflow import MFGraph

#############
direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
isinhw = lambda i, j, h, w: (0 <= i < h) and (0 <= j < w)


n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
C = [[0]*m for _ in range(n)]

mf = MFGraph(n*m+2)
s = n*m
t = s + 1

ret = 0
for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0:
            mf.add_edge(s, i*m+j, 1)
        else:
            mf.add_edge(i*m+j, t, 1)
        if A[i][j] != B[i][j]: ret += 1

for i in range(n):
    for j in range(m):
        if (i+j) % 2 != 0: continue
        if A[i][j] == B[i][j]: continue
        for di, dj in direc:
            ni, nj = i+di, j+dj
            if not isinhw(ni, nj, n, m): continue
            if A[ni][nj] == B[ni][nj]: continue
            if A[ni][nj] == A[i][j]: continue
            mf.add_edge(i*m+j, ni*m+nj, 1)
print(ret-mf.flow(s, t))
