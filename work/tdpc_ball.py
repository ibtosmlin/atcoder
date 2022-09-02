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
n = int(input())
x = list(map(int, input().split()))
x.sort()
mask = sum((1 << xi for xi in x))
N = 1 << 16
dp = [INF] * N
dp[0] = 0
for i in range(1, N):
    mi = i & mask
    nxtv = 10**9
    for j in range(16):
        ret = 0
        for k in {-1, 0, 1}:
            if 0<= j+k < 16:
                ret += dp[mi & ~(1<<(j+k))]
        nxtv = min(nxtv, ret)
    dp[i] = nxtv / 3 + 1
print(dp[N-1])
