# https://atcoder.jp/contests/past15-open/tasks/past202306_l
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from collections import deque

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

G = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if B[i][j] != -1:
            G[i][j] = A[i][j] ^ B[i][j]

def bfs(u):
    E = [[] for _ in range(h+w)]
    for i in range(h):
        for j in range(w):
            c = G[i][j]
            if c == -1: continue
            c = c >> u & 1
            E[i+w].append((j, c))
            E[j].append((i+w, c))
    que = deque()
    seen = [-1] * (h+w)
    for s in range(h+w):
        if seen[s] != -1: continue
        seen[s] = 0
        que.append(s)
        while que:
            x = que.popleft()
            for nx, f in E[x]:
                if seen[nx] == -1:
                    seen[nx] = seen[x] ^ f
                    que.append(nx)
                elif seen[nx] != seen[x] ^ f:
                    return False
    return True

for i in range(30):
    if bfs(i) == False:
        exit(print('No'))
print('Yes')
