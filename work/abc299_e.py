# https://atcoder.jp/contests/abc299/tasks/abc299_e
from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

color = [1] * n
needblack = []
whites = set()

def bfs(p, d):
    if d == 0:
        needblack.append({p})
        return
    depth = [-1] * n
    que = deque([p])
    depth[p] = 0
    while que:
        x = que.popleft()
        for nx in G[x]:
            if depth[nx] != -1: continue
            depth[nx] = depth[x] + 1
            if depth[nx] < d:
                que.append(nx)
    black = set()
    for i in range(n):
        if depth[i] == -1: continue
        if depth[i] < d:
            color[i] = 0
            whites.add(i)
        black.add(i)
    needblack.append(black)

k = int(input())

for _ in range(k):
    p, d = map(int, input().split())
    p -= 1
    bfs(p, d)

for i in range(len(needblack)):
    needblack[i] = needblack[i] - whites
    if len(needblack[i]) == 0:
        print('No')
        exit()

print('Yes')
print(''.join(map(str, color)))