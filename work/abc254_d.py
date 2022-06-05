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

def prime_factorize(n:int) -> dict:
    if n == 1: return dict({1: 1})
    pd = dict()
    for p in range(2, int(n**0.5)+1):
        if n % p != 0: p += 1; continue
        d = 0
        while n % p == 0:
            d += 1
            n //= p
        pd[p] = d
    if n != 1: pd[n] = 1
    return pd


n = int(input())
ret = 0
for i in range(1, n+1):
    r = prime_factorize(i)
    k = 1
    for ri in r:
        if r[ri]%2:
            k *= ri
    for j in range(1, n+1):
        if k*j*j <= n:
            ret += 1
        else:
            break


print(ret)
