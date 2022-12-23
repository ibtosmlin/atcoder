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
s = input()
t = input()

dp = [[""] * (n+1) for _ in range(n+1)]
for l in range(n):
    dp[l][l+1] = s[l]
for d in range(1, n+1):
    for l in range(n):
        r = l + d
        if r > n: break
        dp[l][r] = dp[l][r-1] + dp[r-1][r]
        length = len(dp[l][r])
        for k in range(l, r+1):
            nw = dp[l][k] + dp[k][r]
            nw = nw.replace(t, '')
            if length > len(nw):
                dp[l][r] = nw
#for dpi in dp:
#    print(dpi)
print((n - len(dp[0][n]))//len(t))
