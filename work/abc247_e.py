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
n, x, y = map(int, input().split())
a = list(map(int, input().split()))

posx = -1
posy = -1
posng = -1

ret = 0
for r, ar in enumerate(a):
    if ar < y or ar > x:
        posng = r
    if ar == y:
        posy = r
    if ar == x:
        posx = r
    ret += max(0, min(posx, posy) - posng)

print(ret)