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
n, m = map(int, input().split())

if n > 61: end(0)

add = []
noid = 1
while noid * 2 <= m:
    add.append(noid)
    noid *= 2
add.append(m - noid + 1)

l = len(add)

dp = [[0]*(l+1) for _ in range(n)]
# i番目まで決めてAiがj桁のもの
for i in range(l):
    dp[0][i] = add[i]

for i in range(n-1):
    for j in range(l):
        for k in range(j):
            dp[i+1][j] += dp[i][k] * add[j]
            dp[i+1][j] %= mod1

print(sum(dp[-1])%mod1)
