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
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()

n, k = map(int, input().split())
a = list(map(int1, input().split()))
pt = []
for _ in range(n):
    x, y = map(int, input().split())
    pt.append((x, y))

ret = 0

for i in range(n):
    if i in a: continue
    x0, y0 = pt[i]
    mnd = 10**10
    for ai in a:
        x1, y1 = pt[ai]
        mnd = min(mnd, ((x1-x0)**2 + (y1-y0)**2)**0.5)
    ret = max(ret, mnd)

print(ret)