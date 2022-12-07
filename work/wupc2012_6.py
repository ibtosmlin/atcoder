from collections import defaultdict

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

    def grid_add(self, i, j, ad=1):
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

n = int(input())
mx = 1002
im = Imos(1002, 1002)
pt = []
yonx = defaultdict(set)
xony = defaultdict(set)
for _ in range(n):
    x, y = map(int, input().split())
    x += 1
    y += 1
    pt.append(x*mx +y)
    im.grid_add(x, y)
    yonx[x].add(y)
    xony[y].add(x)
pts = set(pt)

im.accumlate()
ret = 0
yonxkeys = sorted(yonx.keys())
for i, xi in enumerate(yonxkeys):
        for j in range(i):
            xj = yonxkeys[j]
            # xj < xi
            for yi in yonx[xi]:
                for yj in yonx[xj]:
                    if yj >= yi: continue
                    if not xi*mx+yj in pts: continue
                    if not xj*mx+yi in pts: continue
                    if im.count(xj, yj, xi-1, yi-1) >0: continue
                    ret = max(ret, (xi-xj)*(yi-yj))
print(ret)