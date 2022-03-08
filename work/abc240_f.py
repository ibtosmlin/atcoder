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



def solv():
    n, m = map(int, input().split())
    c = []
    y = []
    b = [0]
    a = [0]
    for _ in range(n):
        u, v = map(int, input().split())
        c.append(u)
        y.append(v)
        nb = b[-1] + u*v
        na = a[-1] + b[-1] * v + u*v*(v+1)//2
        b.append(nb)
        a.append(na)

    ret = - 10**10
    for i in range(n):
        ci = c[i]
        bi = b[i]
        ai = a[i]
        yi = y[i]
        ret = max(ret, a[i+1], a[i]+bi+ci)
        if ci<0 and bi>0:
            x = int(-bi//ci)
            for dx in range(-2, 3):
                nx = x+dx
                if 0 < nx < yi:
                    nw = ai + bi * nx + ci * nx*(nx+1)//2
                    ret = max(nw, ret)
    print(ret)


t = int(input())

for _ in range(t):
    solv()
