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
n, m, k = map(int, input().split())
if k == 0:
    print(pow(m, n, mod1))
    exit()

dp = [[0] * (m+1) for _ in range(n)]
sdp = [[0] * (m+1) for _ in range(n)]
for j in range(1, m+1):
    dp[0][j] = 1
for j in range(1, m+1):
    sdp[0][j] = sdp[0][j-1] + dp[0][j]

for i in range(n-1):
    for j in range(1, m+1):
        if m>=k+j-1:
            dp[i+1][j] += sdp[i][m] - sdp[i][k+j-1]
        if j-k>=0:
            dp[i+1][j] += sdp[i][j-k] - sdp[i][0]
        dp[i+1][j] %= mod1
    for j in range(1, m+1):
        sdp[i+1][j] = sdp[i+1][j-1] + dp[i+1][j]
        sdp[i+1][j] %= mod1

print(sum(dp[n-1])%mod1)
