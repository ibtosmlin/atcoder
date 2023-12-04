# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))

m = int(input())
n = int(input())

G = []
for _ in range(n):
    u = list(map(int, input().split()))
    G.append(u)

def dfs(x, y):
    global G
    for dx, dy in direc:
        ret = 0
        nx = x + dx
        ny = y + dy
        if notinhw(nx, ny, n, m): continue
        if G[nx][ny] == 0: continue
        G[nx][ny] = 0
        ret = max(ret, 1+dfs(x, y))
        G[nx][ny] = 1
    return ret

ret = 0
for i in range(n):
    for j in range(m):
        if G[i][j] == 0: continue
        u = dfs(i, j)
        ret = max(ret, u)
print(ret)