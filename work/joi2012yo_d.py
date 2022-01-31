import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
n, k = map(int, input().split())

cond = [list(range(3)) for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    cond[x] = [y - 1]

dp = [[[0] * 3 for __ in range(3)] for _ in range(n+1)]

for j in cond[0]:
    for k in cond[1]:
        dp[2][j][k] = 1

for i in range(2, n):
    for nxt in cond[i]:
        for j in range(3):
            for k in range(3):
                if nxt == j and nxt == k: continue
                dp[i+1][k][nxt] += dp[i][j][k]
                dp[i+1][k][nxt] %= 10000

ret = 0
for dpi in dp[-1]:
    ret += sum(dpi)% 10000
print(ret%10000)