# https://atcoder.jp/contests/nadafes2022_day2/tasks/nadafes2022_day2_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))

from collections import deque
h, w, n = map(int, input().split())
bombs = [(0,0,0,0)]
for _ in range(n):
    c, d, s, t = map(int, input().split())
    c -= 1; d -= 1
    bombs.append((c, d, s, t))
G = [input() for _ in range(h)]

INF = 10**18
dist = [[INF] * (n+1) for _ in range(n+1)]

for x, (i, j, _, __) in enumerate(bombs):
    que = deque([(i, j)])
    seen = [[INF] * w for _ in range(h)]
    seen[i][j] = 0
    while que:
        ci, cj = que.popleft()
        for di, dj in direc:
            ni = ci + di
            nj = cj + dj
            if notinhw(ni, nj, h, w): continue
            if seen[ni][nj] != INF: continue
            if G[ni][nj] == "#": continue
            seen[ni][nj] = seen[ci][cj] + 1
            que.append((ni, nj))
    for y, (u, v, _, __) in enumerate(bombs):
        dist[x][y] = seen[u][v]


dp = [[INF] * (n+1) for _ in range(1<<(n+1))]
# dp[s][j]   sまでみて、今jに居る時の最短の時間

dp[1][0] = 0

for s in range(1<<(n+1)):
    for x in range(n+1):
        if dp[s][x] == INF: continue
        for y in range(n+1):
            _, __, fm, to = bombs[y]
            if s & (1<<y): continue
            ns = s | 1<<y
            tmp = dp[s][x] + dist[x][y]
            if tmp > to:
                continue
            elif tmp >= fm:
                dp[ns][y] = min(tmp, dp[ns][y])
            else:
                tmp = fm + int(tmp%2!=fm%2)
                if tmp <= to:
                    dp[ns][y] = min(tmp, dp[ns][y])

ret = 0
for s in range(1<<(n+1)):
    for x in range(n+1):
        if dp[s][x] == INF: continue
        ret = max(ret, bin(s).count('1'))
print(ret-1)
