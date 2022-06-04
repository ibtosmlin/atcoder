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
h, w = map(int, input().split())
r,c =map(int, input().split())

d = [(1, 0), (-1, 0), (0,1), (0, -1)]

ret = 0
for i in range(4):
    dx, dy = d[i]
    if not (1<=r+dx<=h): continue
    if not (1<=c+dy<=w): continue
    ret += 1
print(ret)
