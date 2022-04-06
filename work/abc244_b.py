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
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'

n = int(input())
t = input()
dx = 1
dy = 0
x = 0
y = 0
for ti in t:
    if ti == 'S':
        x += dx
        y += dy
    else:
        if dx == 1 and dy == 0:
            dx, dy = 0, -1
        elif dx == 0 and dy == -1:
            dx, dy = -1, 0
        elif dx == -1 and dy == 0:
            dx, dy = 0, 1
        else:
            dx, dy = 1, 0
print(x,y)