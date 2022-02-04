import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
x = 1
y = 1
for i in range(65):
    x += y
    y += x
print(x, y)
x, y = 314159265, 358979323
u, v = 846264338, 327950288
z, w = 419716939,  937510582

dx = x-u
dy = y-v
dz = z-u
dw = w-v

print(dx, dy)
print(dz, dw)