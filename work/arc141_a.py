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

def make_divisors(n:int) -> list:
    lower_divisors, upper_divisors = [], []
    for i in range(1, int(n**0.5)+1):
        if n % i != 0: i += 1; continue
        lower_divisors.append(i)
        j = n // i
        if i != j: upper_divisors.append(j)
    return lower_divisors + upper_divisors[::-1]

def f(n):
    d = len(n)
    nn = int(n)
    ret = int('9' * (d-1))
    m = make_divisors(d)
    for mi in m[:-1]:
        x = n[:mi]
        y = str(int(x)-1)
        if len(y) != mi:
            y = x

        nx = int(x * (d//mi))
        ny = int(y * (d//mi))

        if nx <= nn:
            ret = max(nx, ret)
        if ny <= nn:
            ret = max(ny, ret)
    return ret

t = int(input())
for _ in range(t):
    print(f(input()))
#    f(input())