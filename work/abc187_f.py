# https://atcoder.jp/contests/abc187/tasks/abc187_f
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
edges = [0] * n
for _ in range(m):
   a, b = map(int1, input().split())
   edges[a] |= 1 << b
   edges[b] |= 1 << a

dp = [False] * (1<<n)
dp[0] = True

for s in range(1<<n):
    if dp[s] == False: continue
    for i in range(n):  # next
        if s >> i & 1: continue
        dp[s|1<<i] |= edges[i] & s == s

INF = 100
cdp = [INF] * (1<<n)
cdp[0] = 0

for s in range(1, 1<<n):
    if dp[s]: cdp[s] = 1
    v = s
    while v:
        v = (v-1) & s
        cdp[s] = min(cdp[s], cdp[v] + cdp[s^v])
print(cdp[-1])
