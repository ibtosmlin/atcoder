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
a = [[0] * n for _ in range(n)]
for i in range(n-1):
    ai = list(map(int, input().split()))
    for j in range(len(ai)):
        a[i][i+j+1] = ai[j]
        a[i+j+1][i] = ai[j]

m = pow(3, n)
ret = -INF
for i in range(m):
    nwi = i
    gp = [[] for _ in range(3)]
    for j in range(n):
        nwi, bit = divmod(nwi, 3)
        gp[bit].append(j)
    nw = 0
    for gpi in gp:
        for u in range(len(gpi)):
            for v in range(u):
                nw += a[gpi[v]][gpi[u]]
    ret = max(ret, nw)

print(ret)