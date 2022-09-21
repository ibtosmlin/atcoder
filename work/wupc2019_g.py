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
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
n, m = map(int, input().split())
a = list(map(int, input().split()))
ra = [[0] * (m+1) for _ in range(n)]
for i, ai in enumerate(a):
    ra[ai][i] = 1
for i in range(n):
    for j in range(m)[::-1]:
        ra[i][j] += ra[i][j+1]

un = [[0] * n for _ in range(n)]
# un[i][j]  iを選んだ時にjの人の不満度
for i in range(n):
    for j in range(n):
        if i == j: continue
        cnt = 0
        for k in range(m):
            if a[k] == j:
                cnt += ra[i][k]
        un[i][j] = cnt

dp = [INF] * (1<<n)
dp[0] = 0
ret = INF
for s in range(1,1<<n):
    mi = INF
    for i in range(n):
        if s>>i & 1 == 0: continue
        now = dp[s & ~(1<<i)]
        for j in range(n):
            if s>>j & 1 ==0:
                now += un[i][j]
        mi = min(mi, now)
    dp[s] = mi
print(dp[-1])



#    0 1 0 0 1
#  0|3 2 2 1 0
#  1|2 2 1 1 1
