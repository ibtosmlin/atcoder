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


n = int(input())

def fx(a, b):
    return a**3 + (a**2) * b +(b**2) * a + b**3

def isx(a):
    a3 = a**3
    a2 = a**2
    ok = 10**6
    ng = 0
    while ok-ng>1:
        mid = (ok+ng) // 2
        if a3+ a2*mid + a*mid*mid + mid**3 >= n:
            ok = mid
        else:
            ng = mid
    return a3+ a2*ok + a*ok*ok + ok**3


ret = INF
for a in range(10**6+1):
    x = fx(a, 0)
    if x >= n:
        ret = min(x, ret)
        break
    else:
        ret = min(isx(a), ret)

print(ret)