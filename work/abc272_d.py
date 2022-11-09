# https://atcoder.jp/contests/abc272/tasks/abc272_d
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

direc = []
for di in range(401):
    for dj in range(401):
        if di ** 2 + dj ** 2 == m:
            direc.append((di, dj))
            direc.append((di, -dj))
            direc.append((-di, dj))
            direc.append((-di, -dj))

dp = [[-1] * n for _ in range(n)]
dp[0][0] = 0
que = deque([(0,0)])
while que:
    i, j = que.popleft()
    for di, dj in direc:
        ni = i + di
        nj = j + dj
        if not isinhw(ni, nj, n, n): continue
        if dp[ni][nj] != -1: continue
        dp[ni][nj] = dp[i][j] + 1
        que.append((ni, nj))

for dpi in dp:
    print(*dpi)
