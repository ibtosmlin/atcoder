# https://atcoder.jp/contests/abc278/tasks/abc278_b
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
H, M = map(int, input().split())

for i in range(24*60):
    now = H*60 + M + i
    now %= 24*60
    h, m = divmod(now, 60)
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    hh = h[0] + m[0]
    mm = h[1] + m[1]
    x = int(hh)
    y = int(mm)
    if 0<= x <= 23 and 0<=y <= 59:
        print(h, m)
        exit()