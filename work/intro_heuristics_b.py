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

connum = 26
d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]

t = [int1(input()) for _ in range(d)]

def score(t):
    sp_get = 0 # satisfy_point, unsatisfy_point
    sp_lost = 0
    last = [-1] * connum
    for di, ti in enumerate(t):
        last[ti] = di
        sp_get += s[di][ti]
        sp_lost += sum((c[tj] * (di - last[tj]) for tj in range(connum)))
        sp = sp_get - sp_lost
        print(sp)
    return sp

score(t)