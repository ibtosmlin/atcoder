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

inv2 = modinv(2, mod1)

def g(n):
    s = len(str(n))-1
    x = 10**s-1
    cnt = n-x
    ret = cnt*(cnt+1) // 2
    ret %= mod1
    return ret

def gk(k):
    x = 10**k - 1
    return g(x)

n = int(input())
k = len(str(n))

ret = g(n)
for i in range(1, k):
    ret += gk(i)
    ret %= mod1
print(ret)
