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
from fractions import Fraction
n, k = map(int, input().split())
if k == 1:
    end('Infinity')

pts = []
for _ in range(n):
    x, y = map(int, input().split())
    pts.append((x, y))

dicount = defaultdict(int)
for i, (x0, y0) in enumerate(pts):
    otpts = defaultdict(int)
    for j, (xj, yj) in enumerate(pts):
        if j == i: continue
        dx, dy = xj-x0, yj-y0
        if dx == 0:
            dy = 1
        else:
            dy = Fraction(dy, dx)
            dx = 1
        otpts[(dx, dy)] += 1
    for _, v in otpts.items():
        v += 1
        if v >= k:
            dicount[v] += 1

ret = 0
for ky, v in dicount.items():
    ret += v//ky
print(ret)
