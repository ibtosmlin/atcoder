# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ed
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
dmx = 30
n, k = map(int, input().split())
# f(i)  [0, n] -> [0, n]
def f(i):
    return i - sum(map(int, list(str(i))))

dp = [[0] * (n+1) for _ in range(dmx+1)]

for i in range(n+1):
    dp[0][i] = f(i)

for d in range(0, dmx):
    for i in range(n+1):
        dp[d+1][i] = dp[d][dp[d][i]]

def fk(i, k):
    for d in range(dmx):
        if k >> d & 1:
            i = dp[d][i]
    return i

for i in range(1, n+1):
    print(fk(i, k))