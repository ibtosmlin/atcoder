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
n, m ,q = map(int, input().split())

cond = defaultdict(int)
for _ in range(q):
    a, b, c, d = map(int, input().split())
    cond[(a-1, b-1, c)] = d

d = defaultdict(int)
d["0"] = 0


for b in range(1, n):
    nd = defaultdict(int)
    for A, v in d.items():
        for Ab in range(int(A[-1]), m):
            nA = A + str(Ab)
            nd[nA] = v
            for a in range(b):
                nd[nA] += cond[(a, b, Ab-int(A[a]))]
    d = nd.copy()
print(max(d.values()))