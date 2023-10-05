# https://atcoder.jp/contests/abc320/tasks/abc320_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(m):
    a, b, dx, dy = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, [dx, dy]))
    G[b].append((a, [-dx, -dy]))

XY = [None for _ in range(n)]
XY[0] = [0, 0]
que = deque([0])
while que:
    x = que.popleft()
    for nx, dxy in G[x]:
        if XY[nx] != None: continue
        XY[nx] = [XY[x][i] + dxy[i] for i in range(2)]
        que.append(nx)
for u in XY:
    if u:
        print(*u)
    else:
        print('undecidable')
