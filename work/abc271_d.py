# https://atcoder.jp/contests/abc271/tasks/abc271_d
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
n, s = map(int, input().split())
dp = [[False] * (s+1) for _ in range(n+1)]
dp[0][0] = True

card = []
for i in range(n):
    a, b = map(int, input().split())
    card.append((a, b))
    for s in range(1, s+1):
        if s-a>=0:
            dp[i+1][s] |= dp[i][s-a]
        if s-b>=0:
            dp[i+1][s] |= dp[i][s-b]

if dp[n][s]:
    print('Yes')
    ret = []
    nw = s
    for i in range(n)[::-1]:
        a, b = card[i]
        if dp[i][nw-a]:
            ret.append('H')
            nw -= a
        else:
            ret.append('T')
            nw -= b
    print("".join(ret)[::-1])



else:
    print('No')
