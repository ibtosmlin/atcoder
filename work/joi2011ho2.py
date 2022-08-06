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
n, k = map(int, input().split())

books = [[] for _ in range(10)]
for _ in range(n):
    c, g = map(int, input().split())
    g -= 1
    books[g].append(c)

for booki in books:
    booki.sort(reverse=True)

ps = [[(0, 0)] for _ in range(10)]
for j, booki in enumerate(books):
    t = 0
    add = 0
    for i, v in enumerate(booki):
        t += v
        ps[j].append((i+1, t + i * (i+1)))

dp = [-1] * (k+1)
dp[0] = 0
for i, psi in enumerate(ps):
    for ki in range(k+1)[::-1]:
        for c, v in psi[::-1]:
            if ki - c >= 0 and dp[ki-c] >= 0:
                dp[ki] = max(dp[ki], dp[ki-c] + v)
print(dp[k])
