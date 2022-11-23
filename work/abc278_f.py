# https://atcoder.jp/contests/abc278/tasks/abc278_f
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
n = int(input())
G = [[] for _ in range(n)]
s = []
for _ in range(n):
    si = input()
    s.append((si[0], si[-1]))
for i in range(n):
    for j in range(n):
        if i == j: continue
        if s[j][0] == s[j][1]:
            G[i].append(j)

dp = [False] * (1<<n)
dp[0] = False
for j in range(n):
    dp[1 << j] = True

for i in range(1, 1<<n):
    for j in range(n):
        if i >> j & 1:
            for k in G[j]:
                if i>>j & 1 == 0:
                    dp[i|1<<j] = dp[i|1<<j] & dp[i]

print(dp[1<<n-1])