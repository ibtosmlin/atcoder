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
x, a, d, n = map(int, input().split())

if d == 0:
    print(abs(x-a))
    exit()

b = a + (n-1)*d
mn = min(a, b)
mx = max(a, b)
if x<mn:
    print(mn-x)
    exit()
elif x > mx:
    print(x-mx)
    exit()


for i in range(abs(d)):
    xp = x + i
    xm = x - i
    if (xp - a)%d == 0 and 0<=(xp - a)//d<n:
        print(i)
        exit()
    if (xm - a)%d == 0 and 0<=(xm - a)//d<n:
        print(i)
        exit()
