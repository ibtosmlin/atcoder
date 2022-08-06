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
n, k = map(int, input().split())
dp = [[0] *2 for _ in range(n)]
# dp[i][j] i番目の駅で止まるj = 0 止まらない j = 1
dp[0][0] = 1

for i in range(1, n):
    dp[i][1] = dp[i-1][0] + dp[i-1][1]
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    if i >= k:
    dp[i][0] = dp[i-k]



print(dp)

print(dp[n-1][0])
