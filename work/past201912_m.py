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
n, m = map(int, input().split())
monst = [tuple(map(int, input().split())) for _ in range(n)]
suppm = [tuple(map(int, input().split())) for _ in range(m)]

def is_ok(mon, x):
    d = []
    for a, b in mon:
        d.append(b - a * x)
    d.sort(reverse=True)
    return sum(d[:5]) >= 0

def bi(monst):
    ok = 0
    ng = 100001

    while abs(ok - ng) > 0.00000001:
        mid = (ok + ng) / 2
        if is_ok(monst, mid): ok = mid
        else: ng = mid

    return ok

ret = bi(monst)
for sup in suppm:
    ret = max(ret, bi(monst + [sup]))

print(ret)