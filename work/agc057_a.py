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

def f(l, r):
    ok = r
    ng = l-1
    while ok-ng>1:
        mid = (ok+ng)//2
        mst = str(mid)
        fg = True
        for i in range(10):
            if int(mst + str(i)) <=r:
                fg = False
                break
            if i and int(str(i) + mst) <=r:
                fg = False
                break
        if fg:
            ok = mid
        else:
            ng = mid
    return r - ng 



t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(f(l, r))
