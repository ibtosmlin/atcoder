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
n, m, k = map(int, input().split())
a = list(map(int, input().split()))

INF = 1<<60
dp = [[-INF] * k for _ in range(m+1)]
dp[0][0] = 0

for i, ai in enumerate(a):
    ndp = [[-INF] * k for _ in range(m+1)]
    mx = -INF
    for mi in range(1, m+1):
        for ki in range(k):
            mx = max(mx, dp[mi-1][ki] + ai)
        ndp[mi][0] = mx
    for mi in range(m+1):
        for ki in range(1, k):
            ndp[mi][ki] = max(ndp[mi][ki], dp[mi][ki-1])
    dp = ndp
ret = max(dp[m])
print(-1 if ret < 0 else ret)
