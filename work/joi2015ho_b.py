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
n = int(input())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)

# dp[l][r] = A[l]からA[r]のピースが残ってる時のJOIくんの取り分の最大値
dp = [[-INF] * n for _ in range(n)]
for d in range(n):
    turn = d%2
    for l in range(2*n):
        r = l + d
        if d == 0:
            if turn == 0:
                dp[l%n][r%n] = a[l%n]
            else:
                dp[l%n][r%n] = 0
        else:
            if turn == 0:
                dp[l%n][r%n] = max(dp[l%n][r%n], dp[(l+1)%n][r%n]+a[l%n], dp[l%n][(r-1)%n]+a[r%n])
            else:
                if a[l%n] >= a[(r+1)%n]:
                    dp[l%n][r%n] = max(dp[l%n][r%n], dp[(l+1)%n][r%n])
                if a[(l-1)%n] <= a[r%n]:
                    dp[l%n][r%n] = max(dp[l%n][r%n], dp[l%n][(r-1)%n])

ret = 0
for i in range(n):
    ret = max(ret, dp[i][(i+n-1)%n])
print(ret)