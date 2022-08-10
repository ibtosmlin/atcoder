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
n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ret = [False] * n

ay = []
for i in range(n):
    if ret[i]: continue
    ay.append((-a[i], i))
ay.sort()
for i in range(x):
    ret[ay[i][1]] = True


by = []
for i in range(n):
    if ret[i]: continue
    by.append((-b[i], i))
by.sort()
for i in range(y):
    ret[by[i][1]] = True

tot = []
for i in range(n):
    if ret[i]: continue
    tot.append((-a[i]-b[i], i))
tot.sort()
for i in range(z):
    ret[tot[i][1]] = True

for i, ri in enumerate(ret):
    if ri:
        print(i+1)