# https://atcoder.jp/contests/code-thanks-festival-2018/tasks/code_thanks_festival_2018_e
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
# dp[i][j] := 整数iまで書かれていて、整数iの個数がjである組み合わせ
t = int(input())
a = list(map(int, input().split()))
dp = [[0] * 100000 for _ in range(t+1)]
dp[0][0] = 1
for i, ai in enumerate(a):
    num = i+1
    for j in range(100000):
        for k in range(ai+1):
            if j+k <= 300:
                dp[i+1][j+k] += dp[i][j]
                dp[i+1][j+k] %= mod
    for j in range(1, 100000)[::-1]:
        dp[i+1][j-1] += dp[i+1][j]
        dp[i+1][j-1] %= mod

for dpi in dp:
    print(dpi[1])
#print(dp)
