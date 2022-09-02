from collections import defaultdict, Counter, deque
def end(r=-1): print(r); exit()
direc = {(1, 0), (0, 1), (-1, 0), (0, -1)} #+ [(1, 1), (1, -1), (-1, 1), (-1, -1)]
h, w, k = map(int, input().split())
x, y, u, v = tuple(map(int, input().split()))
x -= 1
y -= 1
u -= 1
v -= 1

g = [list(input()) for _ in range(h)]

INF = 10**9
que = deque()
seen = [[INF] * w for _ in range(h)]
que.append((x, y, 0))
seen[x][y] = 0

while que:
    i, j, c = que.popleft()
    for di, dj in direc:
        for t in range(k):
            ni = i + di * (1+t)
            nj = j + dj * (1+t)
            nc = c+1
            if not (0<=ni<h and 0<=nj<w): break
            if g[ni][nj] == '@': break
            if nc > seen[ni][nj]:
                break
            elif seen[ni][nj] == INF:
                seen[ni][nj] = nc
                que.append((ni, nj, c+1))
            if ni == u and nj == v:
                end(nc)
end(-1)
