# https://atcoder.jp/contests/abc272/tasks/abc272_e
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
a = list(map(int, input().split()))
ret = [set() for _ in range(m+1)]
for i, ai in enumerate(a):
    u = i + 1
    for mi in range(max(1, max(0,-ai)//u-1), min(m+1, max(0, (n - ai)) // u + 1)):
        if ai + u*mi > n: break
        if 0<= ai + u*mi <= n:
            ret[mi].add(ai + u*mi)

for ri in ret[1:]:
    for i in range(n+1):
        if i in ri: continue
        print(i)
        break
