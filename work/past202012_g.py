import sys
sys.setrecursionlimit(10**8)

direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}

h, w = map(int, input().split())
g = [input() for _ in range(h)]
tot = 0
for gi in g:
    tot += gi.count('#')

seen = [[False] * w for _ in range(h)]
ret = []

def dfs(i, j):
    ret.append((i, j))
    seen[i][j] = True
    if len(ret) == tot:
        print(tot)
        for x, y in ret:
            print(x+1, y+1)
        exit()
    for dh, dw in direc:
        nh, nw = i + dh, j + dw
        if not (0 <= nh < h and 0 <= nw < w): continue
        if seen[nh][nw]:continue
        if g[nh][nw] == '.': continue
        dfs(nh, nw)
    ret.pop()
    seen[i][j] = False

for i in range(h):
    for j in range(w):
        if g[i][j] == '.': continue
        dfs(i, j)