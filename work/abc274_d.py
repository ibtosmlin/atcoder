# https://atcoder.jp/contests/abc274/tasks/abc274_d
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
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
xa = a[0:n:2]
x -= xa[0]
ya = a[1:n:2]
xa = xa[1:]


dp = set([x])
l = len(xa)
for i, xi in enumerate(xa):
    ndp = set()
    for u in dp:
        if abs(u + xi) <= 10 * l:
            ndp.add(u+xi)
        if abs(u - xi) <= 10 * l:
            ndp.add(abs(u-xi))
    dp = ndp

fg = 0 in dp

dp = set([y])
l = len(ya)
for i, xi in enumerate(ya):
    ndp = set()
    for u in dp:
        if abs(u + xi) <= 10 * l:
            ndp.add(u+xi)
        if abs(u - xi) <= 10 * l:
            ndp.add(abs(u-xi))
    dp = ndp

fg2 = 0 in dp
ret = fg and fg2
print('Yes' if ret else 'No')