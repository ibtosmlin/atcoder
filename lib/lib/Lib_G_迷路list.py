#name#
# bfs迷路listタイプ
#description#
# bfs迷路listタイプ
#body#
# https://atcoder.jp/contests/abc007/tasks/abc007_3

h, w = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
s[0] -= 1; s[1] -= 1
t[0] -= 1; t[1] -= 1

s = (s[0]+1) * (w+2) + (s[1]+1)
t = (t[0]+1) * (w+2) + (t[1]+1)

wall = 1                                  # 適宜修正
g = []
g += [wall] * (w + 2)
for i in range(h):
    g.append(wall)
    gi = input()
    for j, gij in enumerate(gi):
        g.append(wall if gij == "#" else 0)  # 適宜修正
    g.append(wall)
g += [wall] * (w + 2)
h, w = h+2, w+2

def bfs(h, w, s, t):
    direc = (-w, w, 1, - 1)
    seen = [-1] * (h*w)
    que = deque([s])
    seen[s] = 0
    while que:
        nw = que.popleft()
        nd = seen[nw]
        for di in direc:
            nx = nw + di
            if seen[nx] != -1 or g[nx] == wall: continue
            que.append(nx)
            seen[nx] = nd + 1
    return seen

print(bfs(h, w, s, t)[t])
#prefix#
# Lib_G_迷路listタイプ
#end#
