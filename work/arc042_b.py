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
x, y = map(int, input().split())
n = int(input())
pt = [tuple(map(int, input().split())) for _ in range(n)]


def d(u, v):
    xu, yu = u
    xv, yv = v
    a = yv-yu
    b = xu-xv
    c = xv*yu-xu*yv
    r = a*x+b*y+c
    r = abs(r)
    r /= (a**2+b**2)**0.5
    return r

ret = 10000
for i in range(n):
        ret = min(ret, d(pt[i%n], pt[(i+1)%n]))

print(ret)