import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()
n = int(input())
ax, ay = map(int1, input().split())
bx, by = map(int1, input().split())
g = [input() for _ in range(n)]
dist = [[INF] * n for _ in range(n)]
dx = [1, -1, 1, -1]
dy = [1, 1, -1, -1]

que = deque([])
dist[ax][ay] = 0
for j in range(4):
    nx = ax + dx[j]
    ny = ay + dy[j]
    if not ((0<= nx < n) and (0<= ny < n)): continue
    if g[nx][ny] == '#': continue
    dist[nx][ny] = 1
    que.append((nx, ny, j))


while que:
    cx, cy, ci = que.popleft()
    for j in range(4):
        nx = cx + dx[j]
        ny = cy + dy[j]
        nd =  + (ci != j)
        if not ((0<= nx < n) and (0<= ny < n)): continue
        if g[nx][ny] == '#': continue
        if nd < dist[nx][ny][j]:
            dist[nx][ny][j] = nd
            que.append((nx, ny, j, nd))


ret = min(dist[bx][by]) + 1
print(-1 if ret == INF else ret)
