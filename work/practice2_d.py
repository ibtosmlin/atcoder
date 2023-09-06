# https://atcoder.jp/contests/practice2/tasks/practice2_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1


from atcoder.maxflow import MFGraph
#############
n, m = map(int, input().split())
mf = MFGraph(n*m+2)
s = n*m
g = n*m + 1
G = [list(input()) for _ in range(n)]
direc = {(1, 0), (0, 1), (-1, 0), (0, -1)}
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))

for i in range(n):
    for j in range(m):
        if G[i][j] == "#": continue
        if (i*m + j) % 2:
            mf.add_edge(s, i*m + j, 1)
        else:
            mf.add_edge(i*m + j, g, 1)
        for di, dj in direc:
            ni = i+di
            nj = j+dj
            # i*m + j <> ni*m+j
            if (i*m + j) % 2:
                if not notisinhw(ni, nj, n, m) and G[ni][nj] == ".":
                    mf.add_edge(i*m + j, ni*m+nj, 1)


print(mf.flow(s, g))
for e in mf.edges():
    if e.flow == 0: continue
    fi, fj = divmod(e.src, m)
    ti, tj = divmod(e.dst, m)
    if e.dst == e.src + 1:
        G[fi][fj] = ">"
        G[ti][tj] = "<"
    if e.dst == e.src + m:
        G[fi][fj] = "v"
        G[ti][tj] = "^"

    if e.src == e.dst + 1:
        G[fi][fj] = "<"
        G[ti][tj] = ">"
    if e.src == e.dst + m:
        G[fi][fj] = "^"
        G[ti][tj] = "v"


for gi in G:
    print(''.join(gi))


#print(mf.progress)