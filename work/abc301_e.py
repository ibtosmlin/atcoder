# https://atcoder.jp/contests/abc301/tasks/abc301_e
from collections import deque
import copy

INF = 10**9
direc = [(1, 0), (0, 1), (-1, 0), (0, -1) ]
h, w, t = map(int, input().split())
G = [list(input()) for _ in range(h)]
candys = []
for i in range(h):
    for j in range(w):
        if G[i][j] == 'S':
            start = (i, j)
        if G[i][j] == 'G':
            goal = (i, j)
        if G[i][j] == 'o':
            candys.append((i, j))

allitems = [start] + candys[:] + [goal]

def bfs(f):
    que = deque()
    que.append(f)
    seen = [[-1] * w for _ in range(h)]
    seen[f[0]][f[1]] = 0
    while que:
        hi, wi = que.popleft()
        for hd, wd in direc:
            hj = hi + hd
            wj = wi + wd
            if hj < 0 or hj >= h or wj < 0 or wj >= w: continue
            if G[hj][wj] == '#': continue
            if seen[hj][wj] != -1: continue
            seen[hj][wj] = seen[hi][wi] + 1
            if seen[hj][wj] < t:
                que.append((hj, wj))
    return seen

n = 2 + len(candys)
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    result = bfs(allitems[i])
    for j in range(i+1, n):
        u, v = allitems[j]
        d = result[u][v]
        if d == -1: continue
        dist[i][j] = dist[j][i] = d

def d(fm, to):
    return dist[fm][to]

dp = [[INF] * n for _ in range(1 << n)]
for first in range(n):
    dp[1 << first][first] = d(0, first)

for s in range(1, 1 << n):
    for fm in range(n):
        if not s >> fm & 1: continue    # fmがsに無い場合->スキップ
        if dp[s][fm] > t: continue   # 到達距離がINF->スキップ
        for to in range(n):
            if s >> to & 1: continue    # すでにtoがsにいる場合->スキップ
            next_s = s | (1 << to)      # toを追加した状態
            dp[next_s][to] = min(dp[next_s][to], dp[s][fm] + d(fm, to))

mask = (1 << (n-1)) - 2
ret = -1
for i in range(1<<n):
    if dp[i][-1] <= t:
        ret = max(bin(mask & i).count("1"), ret)
print(ret)
