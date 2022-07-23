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
n, c = map(int, input().split())
f = [(0, 1) for _ in range(30)]
for i in range(n):
    t, a = map(int, input().split())
    nc = 0
    for j in range(30):
        b0, b1 = f[j]
        ai = (a >> j) & 1
        if t == 1:
            f[j] = (b0 & ai, b1 & ai)
        if t == 2:
            f[j] = (b0 | ai, b1 | ai)
        if t == 3:
            f[j] = (b0 ^ ai, b1 ^ ai)
        nc += f[j][(c >> j) & 1] << j
    c = nc
    print(c)