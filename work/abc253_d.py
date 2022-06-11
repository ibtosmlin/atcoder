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
import math
n, a, b = map(int, input().split())

def cnt(u, cn):
    return u * (cn + 1) * cn // 2
# a
ca = n//a
cb = n//b
gx = a*b // math.gcd(a, b)
cab = n//gx


print(cnt(1, n) - cnt(a, ca) - cnt(b, cb) + cnt(gx, cab))
