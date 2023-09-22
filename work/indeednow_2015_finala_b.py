# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

INF = 100000000000
direc0 = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1)}
direc1 = {(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1)}

notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))

h, w = map(int, input().split())

G = [[0] *  w for _ in range(h)]
R = [[INF] *  w for _ in range(h)]

s = None
t = None
for i in range(h):
    si = input()
    for j, sij in enumerate(si):
        if sij == 's': s = (i, j)
        elif sij == 't':t = (i, j)
        else:
            G[i][j] = int(sij)


from heapq import heapify, heappop, heappush
que=[(0, s)]
R[s[0]][s[1]] = 0

while que:
    d, (i, j) = heappop(que)
    if R[i][j] < d: continue
    if i%2:
        direc = direc0
    else:
        direc = direc1
    for di, dj in direc:
        ni = i + di
        nj = j + dj
        if notinhw(ni, nj, h, w): continue
        nd = R[i][j] + G[ni][nj]
        if R[ni][nj] <= nd:continue
        R[ni][nj] = nd
        heappush(que, (nd, (ni, nj)))

print(R[t[0]][t[1]])


