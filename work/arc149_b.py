# https://atcoder.jp/contests/arc149/tasks/arc149_b
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

from bisect import bisect, bisect_left

def LIS(x:list, fg=1):
    n = len(x)
    res = [0] * n
    dp = []
    for i, xi in enumerate(x):
        # 非減少
        if fg == 0:
            pos = bisect(dp, xi)
        elif fg == 1:
        # 単調増加
            pos = bisect_left(dp, xi)
        res[i] = pos + 1
        if len(dp) <= pos:
            dp.append(xi)
        else:
            dp[pos] = xi
    length = len(dp)
    restore = []
    nw = length
    for i in range(n)[::-1]:
        if nw == res[i]:
            restore.append(x[i])
            nw -= 1
    restore.reverse()
    return length#, restore, dp, res

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = [(ai, bi) for ai, bi in zip(a, b)]
ab.sort()
print(LIS([bi for _, bi in ab]) + n)
