# https://atcoder.jp/contests/abc280/tasks/abc280_d
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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
k = int(input())
##############################
# 素因数分解
# nは10**15くらいまでOK
# returns dict s.t. key = {prime}   value = {degree}
##############################
def prime_factorize(n:int) -> dict:
    if n == 1: return {1: 1}
    pd = dict()
    for p in range(2, int(n**0.5)+1):
        if n % p != 0: continue
        d = 0
        while n % p == 0:
            d += 1
            n //= p
        pd[p] = d
    if n != 1: pd[n] = 1
    return pd

#print(prime_factorize(360))  # 72 = 2**3 * 3**2 * 5**1
                             # {2: 3, 3: 2, 5: 1}
x = prime_factorize(k)

ret = 0
for p, c in x.items():
    nw = 1
    cnt = 0
    for i in range(1, c+1):
        nw *= i*p
        u = i * p
        while u%p == 0:
            u //= p
            cnt += 1
        if cnt >= c:
            break
    ret = max(ret, i*p)
#    print(p,c,nw, cnt)
print(ret)
