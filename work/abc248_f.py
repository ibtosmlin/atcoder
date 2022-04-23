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

n, p = map(int, input().split())
dp = [[0]*2 for j in range(n+1)]

dp[1][0] = 1
dp[0][1] = 1

for i in range(n-1):
    ndp = [[0]*2 for j in range(n+1)]
    for j in range(n+1):
        dp0 = dp[j][0]
        dp1 = dp[j][1]
        ndp[j][1] += dp0 + dp1
        ndp[j][1] %= p
        if j+1<=n:
            ndp[j+1][0] += dp0
            ndp[j+1][1] += dp1
            ndp[j+1][1] += 2*dp1
            ndp[j+1][0] %= p
            ndp[j+1][1] %= p
        if j+2<=n:
            ndp[j+2][0] += 2*dp1
            ndp[j+2][0] %= p
    dp = ndp.copy()

ret = []
for i in range(n-1):
    ret.append(dp[i+1][1])

print(*ret)
