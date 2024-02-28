h, w, n = map(int, input().split())
t = input()
G = [input() for _ in range(h)]
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))
direc = {"D":(1, 0), "U":(-1, 0), "R":(0, 1), "L":(0, -1)}

now = [[0, 0] for _ in range(n+1)]
for i, ti in enumerate(t):
    di, dj = direc[ti]
    now[i+1][0] = now[i][0] + di
    now[i+1][1] = now[i][1] + dj

def isok(i, j):
    for di, dj in now:
        if notinhw(i+di, j+dj, h, w) or G[i+di][j+dj] == "#": return False
    return True

ret = 0
for i in range(h):
    for j in range(w):
        if isok(i, j): ret += 1
print(ret)