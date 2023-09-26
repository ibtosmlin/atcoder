# https://atcoder.jp/contests/nadafes2022_day1/tasks/nadafes2022_day1_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import deque
direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
isinhw = lambda i,j,h,w: (0 <= i < h) and (0 <= j < w)
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))

h,w,k = map(int, input().split())
G = [input() for _ in range(h)]

INF = 10**18
U = [[INF] * w for _ in range(h)]
T = [[INF] * w for _ in range(h)]

que = deque([])
for i in range(h):
    for j in range(w):
        if G[i][j] == '@':
            que.append((i,j))
            T[i][j] = 0

while que:
    i, j = que.popleft()
    for di, dj in direc:
        ni = di+i; nj = dj+j
        if notinhw(ni, nj, h, w): continue
        if T[ni][nj] != INF: continue
        if G[ni][nj] != ".": continue
        T[ni][nj] = T[i][j] + k
        que.append((ni,nj))


que = deque([(0, 0)])
U[0][0] = 0
while que:
    i, j = que.popleft()
    for di, dj in direc:
        ni = di+i; nj = dj+j
        if notinhw(ni, nj, h, w): continue
        if U[ni][nj] != INF: continue
        if G[ni][nj] != ".": continue
        if T[ni][nj] <= U[i][j] + 1: continue
        U[ni][nj] = U[i][j] + 1
        que.append((ni,nj))

print('No' if U[h-1][w-1] == INF else 'Yes')



