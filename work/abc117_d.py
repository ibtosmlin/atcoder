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
n, k = map(int, input().split())
a = list(map(int, input().split()))

D = max(max(a), k).bit_length()
b = [0] * D
for i in range(D):
    cnt = 0
    for ai in a:
        if (ai >> i) & 1:
            cnt += 1
    b[D-1-i] = cnt

dp = [[-INF] * 2 for _ in range(D+1)]
dp[0][0] = 0
for d in range(D):
    sel0 = b[d]
    sel1 = n - sel0
    dp[d+1][1] = max(dp[d+1][1], dp[d][1] * 2 + max(sel1, sel0))
    if k >> (D-1-d) & 1:
        dp[d+1][0] = max(dp[d+1][0], dp[d][0] * 2 + sel1)
        dp[d+1][1] = max(dp[d+1][1], dp[d][0] * 2 + sel0)
    else:
        dp[d+1][0] = max(dp[d+1][0], dp[d][0] * 2 + sel0)
print(max(dp[-1]))