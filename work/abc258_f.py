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

def dis(u, v):
    return abs(u[0] - v[0]) + abs(u[1]-v[1])

def corners(u, b):
    x, y = u
    #
    (x + (b-1))//b * b


def f(b, k, sx, sy, gx, gy):




t = int(input())
for _ in range(t):
    b, k, sx, sy, gx, gy = map(int, input().split())
    print(f(b, k, sx, sy, gx, gy))