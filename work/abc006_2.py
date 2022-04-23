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

memo = [-1] * (n+1)

def f(n):
    if memo[n] != -1:
        return memo[n]
    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1
    memo[n] = (f(n-1) + f(n-2) + f(n-3))%10007
    return memo[n]

print(f(n))