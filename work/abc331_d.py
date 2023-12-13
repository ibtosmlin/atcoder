# https://atcoder.jp/contests/abc331/tasks/abc331_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

class Imos:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        # 拡張grid生成
        self.grid = [[0] * (w+1) for _ in range(h+1)]

    def import_grid(self, grid):
        for i in range(self.h):
            for j in range(self.w):
                self.grid[i+1][j+1] = grid[i][j]

    def grid_add(self, i, j, ad):
        # i, j is 0 index on self.grid
        self.grid[i][j] += ad

    def accumlate(self):
        # 累積和
        for i in range(self.h+1):
            for j in range(1, self.w+1):
                self.grid[i][j] += self.grid[i][j-1]
        for j in range(self.w+1):
            for i in range(1, self.h+1):
                self.grid[i][j] += self.grid[i-1][j]

    def count(self, x, y, u, v):
        if not 0<= x <= u < self.h+1: return 0
        if not 0<= y <= v < self.w+1: return 0
        gd = self.grid
        return gd[u][v] - gd[u][y] - gd[x][v] + gd[x][y]

###############################################
N, Q = map(int, input().split())
G = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        G[i][j] = int(G[i][j] == 'B')

im = Imos(N, N)
im.import_grid(G)
im.accumlate()

def cgd(x, y):
    cx, x = divmod(x, N)
    cy, y = divmod(y, N)
    ret = 0
    ret += im.count(0,0,N,N) * cx * cy
    ret += im.count(0,0,N,y) * cx
    ret += im.count(0,0,x,N) * cy
    ret += im.count(0,0,x,y)
    return ret

def count(x, y, u, v):
    if not 0 <= x <= u : return 0
    if not 0 <= y <= v : return 0
    return cgd(u, v) - cgd(u, y) - cgd(x, v) + cgd(x, y)

for _ in range(Q):
    a, b, c, d = map(lambda x:int(x), input().split())
    print(count(a, b, c+1, d+1))