#name#
# 累積和
#description#
# 累積和
#body#
class imos:
    def __init__(self, grid):
        h = len(grid)
        w = len(grid[0])
        h += 1; w += 1
        self.h = h
        self.w = w
        # 拡張grid生成
        _grid = [[0] * w]
        for gdi in grid:
            _grid.append([0] + gdi)
        # 累積和
        for i in range(1, h):
            for j in range(1, w):
                _grid[i][j] += _grid[i][j-1]
        for j in range(1, w):
            for i in range(1, h):
                _grid[i][j] += _grid[i-1][j]
        self.grid = _grid


    def cnt(self, x, y, u, v):
        if not 0<= x < self.h: return 0
        if not 0<= y < self.w: return 0
        if not 0<= u < self.h: return 0
        if not 0<= v < self.w: return 0
        gd = self.grid
        return gd[u][v] - gd[u][y] - gd[x][v] + gd[x][y]

#prefix#
# Lib_累積和
#end#