# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s
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
n, w = map(int, input().split())
dp = [-1] * (w+1)
dp[0] = 0
for _ in range(n):
    ndp = [-1] * (w+1)
    wi, vi = map(int, input().split())
    for wt in range(w+1)[::-1]:
        ndp[wt] = max(ndp[wt], dp[wt])
        if wt - wi >= 0 and dp[wt - wi] != -1:
            ndp[wt] = max(ndp[wt], dp[wt - wi] + vi)
    dp = ndp

print(max(dp))