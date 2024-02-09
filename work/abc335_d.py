# https://atcoder.jp/contests/abc335/tasks/abc335_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
cnt = 0

direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))

ret = [[None] * n for _ in range(n)]
ret[(n-1)//2][(n-1)//2] = 'T'

nx = 0; ny = 0
ind = 0
ret[0][0] = 1
for i in range(2, n*n):
    nx += direc[ind][0]
    ny += direc[ind][1]
    if notinhw(nx, ny, n, n) or ret[nx][ny] != None:
        nx -= direc[ind][0]
        ny -= direc[ind][1]
        ind = (ind+1)%4
        nx += direc[ind][0]
        ny += direc[ind][1]
    ret[nx][ny] = str(i)

for ri in ret:
    print(*ri)