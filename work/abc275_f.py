# https://atcoder.jp/contests/abc275/tasks/abc275_f
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
# dp[i][j]  iまでみて合計をjにするときの必要な最小値で最後が消されている/いない
dp = [[INF] * 2 for j in range(m+1)]
#dp[0][0] = 0
dp[0][1] = 0
for i in range(n):
    ai = a[i]
    ndp = [[INF] * 2 for j in range(m+1)]
    for j in range(1+m):
        # 取る場合
        if j +ai <= m:
            ndp[j+ai][1] = min(ndp[j+ai][1], dp[j][0], dp[j][1])
        # 取らない場合
        ndp[j][0] = min(ndp[j][0], dp[j][0], dp[j][1] + 1)
    dp = ndp

for i in range(1, m+1):
    ret = min(dp[i])
    print(-1 if ret == INF else ret)
