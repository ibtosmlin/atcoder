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


pts = []
for _ in range(3):
    x, y = map(int, input().split())
    pts.append((x, y))

for i in range(3):
    x, y = pts[i]
    nx, ny = pts[(i+1)%3]
    mx, my = pts[(i+2)%3]
    if x==nx and y == my:
        print(mx, ny)
        exit()
    if x==mx and y == ny:
        print(nx, my)
        exit()
