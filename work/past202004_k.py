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
s = list(input())
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# dp[i][j]  i文字目まで見て、count("(")-count(")") == jとなる最小のコスト

dp = [INF] * 3010
dp[0] = 0
for i, si in enumerate(s):
    ndp = [INF] * 3010
    for j in range(3000):
        if si == '(':
            ndp[j+1] = min(ndp[j+1], dp[j])
            ndp[j] = min(ndp[j], dp[j]+D[i])
            if j > 0:
                ndp[j-1] = min(ndp[j-1], dp[j]+C[i])
        else:
            if j > 0:
                ndp[j-1] = min(ndp[j-1], dp[j])
            ndp[j+1] = min(ndp[j+1], dp[j]+C[i])
            ndp[j] = min(ndp[j], dp[j]+D[i])
    dp = ndp

print(dp[0])
