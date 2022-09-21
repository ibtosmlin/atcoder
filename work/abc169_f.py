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
n, s = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j]  iまで使って合計jができる部分集合の個数

dp = [[0] * 3001 for _ in range(n+1)]
dp[0][0] = 1

for i, ai in enumerate(a):
    # use
    for j in range(0, 3001):
        if j-ai>=0:
            dp[i+1][j] += dp[i][j-ai]    # use
        dp[i+1][j] += dp[i][j] * 2    # notuse
        dp[i+1][j] %= mod1

print(dp[-1][s])