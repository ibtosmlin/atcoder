# https://atcoder.jp/contests/abc331/tasks/abc331_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n, q = map(int, input().split())
P = [[0] * n for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == 'B':
            P[i][j] = 1

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
im = Imos(n, n)
im.import_grid(P)
im.accumlate()

print(im.grid)
def cnt(a, b, c, d):
    ca, a = divmod(a, n)
    c -= ca * n
    cx = c // n

    cb, b = divmod(b, n)
    d -= cb * n
    cy = d // n
