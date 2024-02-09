# https://atcoder.jp/contests/abc339/tasks/abc339_d
d = 100
from collections import deque

def pair(v):
    x, y = divmod(v, d*d)
    x0, x1 = divmod(x, d)
    y0, y1 = divmod(y, d)
    return (x0, x1), (y0, y1)

def vconv(x, y):
    if x > y: x, y = y, x
    return x[0] * (d ** 3) + x[1] * (d ** 2) + y[0] * d + y[1]

notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))


n = int(input())
G = [list(input()) for _ in range(n)]

_st = []
for i in range(n):
    for j in range(n):
        if G[i][j] == 'P':
            _st.append((i, j))
            G[i][j] = '.'
start = vconv(*_st)

dist = dict()
dist[start] = 0
que = deque([start])

direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
while que:
    u = que.popleft()
    x, y = pair(u)
    for di in direc:
        nx = (x[0] + di[0], x[1] + di[1])
        if notinhw(nx[0], nx[1], n, n) or G[nx[0]][nx[1]] == "#": nx = (x[0], x[1])
        ny = (y[0] + di[0], y[1] + di[1])
        if notinhw(ny[0], ny[1], n, n) or G[ny[0]][ny[1]] == "#": ny = (y[0], y[1])
        nu = vconv(nx, ny)
        if nu in dist: continue
        dist[nu] = dist[u] + 1
        que.append(nu)
        if nx == ny:
            exit(print(dist[nu]))
print(-1)
