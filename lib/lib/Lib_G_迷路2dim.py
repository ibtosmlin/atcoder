#name#
# bfs迷路２次元タイプ
#description#
# bfs迷路２次元タイプ
#body#

h, w = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
s[0] -= 1; s[1] -= 1
t[0] -= 1; t[1] -= 1

g = [list(input()) for _ in range(h)]

def bfs(h, w, s, t):
    direc = ((1, 0), (-1, 0), (0, 1), (0, -1))
    seen = [[-1] * w for _ in range(h)]
    que = deque([s])
    seen[s[0]][s[1]] = 0
    while que:
        u, v = que.popleft()
        for du, dv in direc:
            nu = u + du
            nv = v + dv
            if (not isinhw(nu, nv, h, w)) or g[nu][nv] == '#' or seen[nu][nv] != -1:
                continue
            que.append((nu, nv))
            seen[nu][nv] = seen[u][v] + 1
    return seen

print(bfs(h, w, s, t)[t[0]][t[1]])
#prefix#
# Lib_G_迷路2次元タイプ
#end#
