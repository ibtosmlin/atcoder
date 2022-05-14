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

n = int(input())
a = list(map(int, input().split()))

#dp[i][j]  i番目の行動をしたかどうかj=0,j=1かどうか。


dp0 = [[INF]*2 for _ in range(n)]
dp1 = [[INF]*2 for _ in range(n)]

dp0[0] = [0, INF]
dp1[0] = [INF, a[0]]

for i in range(1, n):
    ai = a[i]
    dp0[i][1] = min(dp0[i][1], dp0[i-1][0] + ai)
    dp0[i][1] = min(dp0[i][1], dp0[i-1][1] + ai)
    dp0[i][0] = min(dp0[i][0], dp0[i-1][1])
    dp1[i][1] = min(dp1[i][1], dp1[i-1][0] + ai)
    dp1[i][1] = min(dp1[i][1], dp1[i-1][1] + ai)
    dp1[i][0] = min(dp1[i][0], dp1[i-1][1])

print(min(dp0[-1][1], dp1[-1][0], dp1[-1][1]))

