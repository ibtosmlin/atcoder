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

n, m ,k = map(int, input().split())

dp = [0] * 2510
dp[0] = 1
for i in range(n):
    ndp = [0] * 2510
    for ai in range(1, m+1):
        for j in range(2510):
            if j+ai < 2510:
                ndp[j+ai] += dp[j]
                ndp[j+ai] %= mod1
    dp = ndp.copy()

print(sum(dp[:k+1])%mod1)