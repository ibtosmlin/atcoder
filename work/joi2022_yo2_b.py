# https://atcoder.jp/contests/joi2022yo2/tasks/joi2022_yo2_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
from collections import deque

direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))

h, w = map(int, input().split())
G = [input() for _ in range(h)]
dp = [[-1] * w for _ in range(h)]
dp[0][0] = 0
que =deque([])
que.append((0,0))
while que:
    u, v = que.popleft()
    for du, dv in direc:
        nu = u + du
        nv = v + dv
        if notinhw(nu, nv, h, w): continue
        if G[nu][nv] == G[u][v]: continue
        if dp[nu][nv] != -1: continue
        dp[nu][nv] = dp[u][v] + 1
        que.append((nu, nv))

print(dp[-1][-1])
