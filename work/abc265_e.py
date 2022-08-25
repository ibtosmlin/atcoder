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

n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
direc = [(a, b), (c, d), (e, f)]
bump = set(tuple(map(int, input().split())) for _ in range(m))

dp = [[0] * (n+1) for i in range(n+1)]
dp[0][0] = 1

for t in range(n):
    ndp = [[0] * (n+1) for i in range(n+1)]
    for u in range(t+1):
        for v in range(t+1):
            w = t - u - v
            if w < 0: continue
            cnt = dp[u][v]
            x = u * a + v * c + w * e
            y = u * b + v * d + w * f
            if (x+a, y+b) not in bump:
                ndp[u+1][v] += cnt
                ndp[u+1][v] %= mod1
            if (x+c, y+d) not in bump:
                ndp[u][v+1] += cnt
                ndp[u][v+1] %= mod1
            if (x+e, y+f) not in bump:
                ndp[u][v] += cnt
                ndp[u][v] %= mod1
    dp = ndp

ret = 0
for i in range(n+1):
    for j in range(n+1):
        ret += dp[i][j]
        ret %= mod1
print(ret)
