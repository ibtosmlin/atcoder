# https://atcoder.jp/contests/past202109-open/tasks/past202109_m
from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

seen = [[None] *2 for _ in range(n)]
que = deque([(0, 0)])
seen[0][0] = 0

while que:
    x, t = que.popleft()
    c = seen[x][t]
    nt = 1 - t
    for nx, w in G[x]:
        if seen[nx][nt] == None:
            seen[nx][nt] = w - c
            que.append((nx, nt))
        else:
            if seen[nx][nt] != w - c:
                exit(print(-1))

x = -1
for i in range(n):
    a, b = seen[i]
    if a != None and b != None:
        if (b-a)%2 or (b-a) < 0: exit(print(-1))
        x = (b-a) // 2
        break

if x == -1:
    # 片側のみ
    x = max(0, -min([seen[i][0] for i in range(n) if seen[i][0] != None]))
    for i in range(n):
        a, b = seen[i]
        if b == None: continue
        if b - x < 0: exit(print(-1))

else:
    for i in range(n):
        a, b = seen[i]
        if a != None and b != None:
            if x + a < 0 or x + a != b-x: exit(print(-1))
        elif a != None:
            if b - x < 0: exit(print(-1))
        elif b != None:
            if a + x < 0: exit(print(-1))


ret = [0] * n
for i in range(n):
    a, b = seen[i]
    if a != None:
        ret[i] = a+x
    else:
        ret[i] = b-x
print('\n'.join(map(str, ret)))