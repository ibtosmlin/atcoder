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
n = int(input())
a = list(map(int, input().split()))
dp = [[[0] * (n+1) for _ in range(n+1)] for __ in range(n+1)]
for i in range(1, n+1):
    dp[i][0][0] = 1
# dp[i][j][k]  iで割ったときに、j個合計の余りがk
for ai in a:
    ndp = [[[0] * (n+1) for _ in range(n+1)] for __ in range(n+1)]
#選ぶ
    for i in range(1, n+1):
        for j in range(n):
            for k in range(i):
                x = dp[i][j][k]
                nk = (k + ai) % i
                ndp[i][j][k] += x
                ndp[i][j][k] %= mod1
                ndp[i][j+1][nk] += x
                ndp[i][j+1][nk] %= mod1
    dp = ndp


ret = 0
for i in range(1, n+1):
    ret += dp[i][i][0]
    ret %= mod1

print(ret)

