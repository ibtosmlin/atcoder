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
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
n, x = map(int, input().split())

dp = [False] * (x+1)
dp[0] = True
for i in range(n):
    ndp = [False] * (x+1)
    ai, bi = map(int, input().split())
    for j in range(x)[::-1]:
        if not dp[j]: continue
        if j+ai<=x:
            ndp[j+ai] = True
        if j+bi<=x:
            ndp[j+bi] = True
    dp = ndp[:]
ret = dp[x]
print('Yes' if ret else 'No')