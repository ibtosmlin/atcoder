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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

seen = [-1] * n
cnt = [0, 0]

def bfs(x):
    global seen
    global cnt
    seen[x] = 0
    cnt = [0, 0]
    cnt[0] += 1
    que = deque()
    que.append((i, 0))
    fg = True
    while que:
        nx, fx = que.popleft()
        for y in edges[nx]:
            if seen[y] == -1:
                seen[y] = 1-fx
                cnt[1-fx] += 1
                que.append((y, 1-fx))
            elif seen[y] == 1-fx:
                continue
            else:
                return False
    return True

pat = []
for i in range(n):
    if seen[i] != -1: continue
    if bfs(i):
        pat.append(cnt[:])

p0 = n//3
p1 = n // 3 + int(n%3 >= 1)
p2 = n // 3 + int(n%3 == 2)

dp = [[False] * (p2+1) for _ in range(p1+1)]
dp[0][0] = True

for u, v in pat:
    for i in range(p1+1)[::-1]:
        for j in range(p2+1)[::-1]:
            if dp[i][j] == False: continue
            if i + u <= p1 and j + v <= p2:
                dp[i+u][j+v] |= True
            if i + v <= p1 and j + u <= p2:
                dp[i+v][j+u] |= True

if dp[p1][p2]:
    print('Yes')
else:
    print('No')