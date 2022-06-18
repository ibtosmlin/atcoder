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

invs = [1]
for i in range(210):
    invs.append(modinv(i+1, mod1))


def nCr(n, r):
    if n == 1:
        return 1
    if r == 0:
        return 1
    x = 1
    for i in range(r):
        x *= n-i
        x *= invs[i+1]
        x %= mod1
    return x


n, k = map(int, input().split())
a = list(map(int, input().split()))
a[0] = a[0] - (k+sum(a[1:]))
if a[0] < 0:
    end(0)
ret = 1
for ai in a:
    ret *= nCr(ai+k-1, k-1)
    ret %= mod1
print(ret)


22
12
10
14
4
8

