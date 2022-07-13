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
a = list(map(int, input().split()))
d = defaultdict(list)
for i, ai in enumerate(a):
    d[ai].append(i)


ret = n * (n-1) * (n-2) // 6

for aj, l in d.items():
    L = len(l)
    for sm, j in enumerate(l):
        lg = len(l) - sm - 1
        ret -= sm * (n - 1 - j)
        ret -= j * lg
        if sm < len(l) - 1:
            ret -= (sm +1) * lg * (l[sm+1] - l[sm] - 1)

for di, vi in d.items():
    vi = len(vi)
    ret += vi * (vi-1) * (vi -2) // 6

print(ret)
