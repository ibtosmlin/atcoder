# https://atcoder.jp/contests/abc317/tasks/abc317_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

h, w = map(int, input().split())
G = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if G[i][j] == "S": st = (i, j)
        if G[i][j] == "G": gl = (i, j)

"tate"
for i in range(h):
    state = False
    for j in range(w):
        if G[i][j] == ">":
            state = True
        elif G[i][j] in "<^v#":
            state = False
        elif G[i][j] == "." and state:
            G[i][j] = "!"

    state = False
    for j in range(w)[::-1]:
        if G[i][j] == "<":
            state = True
        elif G[i][j] in ">^v#":
            state = False
        elif G[i][j] == "." and state:
            G[i][j] = "!"

"yoko"
for j in range(w):
    state = False
    for i in range(h):
        if G[i][j] == "v":
            state = True
        elif G[i][j] in "^#><":
            state = False
        elif G[i][j] == "." and state:
            G[i][j] = "!"

    state = False
    for i in range(h)[::-1]:
        if G[i][j] == "^":
            state = True
        elif G[i][j] == "." and state:
            G[i][j] = "!"
        elif G[i][j] in "v<>#":
            state = False



from collections import defaultdict, Counter, deque
seen = [[-1]*w for _ in range(h)]
que = deque([])
seen[st[0]][st[1]] = 0
que.append(st)

direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}

def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))

while que:
    u, v = que.popleft()
    for du, dv in direc:
        nu = u + du
        nv = v + dv
        if notisinhw(nu, nv, h, w): continue
        if seen[nu][nv] != -1: continue
        if G[nu][nv] != "." and G[nu][nv] != "G": continue
        seen[nu][nv] = seen[u][v] + 1
        que.append((nu, nv))

print(seen[gl[0]][gl[1]])


