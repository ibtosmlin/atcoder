# https://atcoder.jp/contests/abc298/tasks/abc298_e
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()

n, a, b, p, q = map(int, input().split())
invp = modinv(p, mod1)
invq = modinv(q, mod1)
dp = [[[0] * 2 for _ in range(n+1)] for __ in range(n+1)]
dp[a][b][0] = 1
for i in range(n):
    for j in range(n):
        for d in range(1, p+1):
            dp[min(i+d, n)][j][1] = (dp[min(i+d, n)][j][1] + invp * dp[i][j][0]) % mod1
        for d in range(1, q+1):
            dp[i][min(j+d, n)][0] = (dp[i][min(j+d, n)][0] + invq * dp[i][j][1]) % mod1

ret = 0
for j in range(n):
    ret += dp[n][j][1]
    ret %= mod1
print(ret)
