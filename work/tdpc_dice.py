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
n, d = map(int, input().split())

two = 0
three = 0
five = 0
while d%2 == 0:
    two += 1
    d //= 2
while d%3 == 0:
    three += 1
    d //= 3
while d%5==0:
    five += 1
    d //= 5
if d != 1: end(0)

n2 = [0, 0, 1, 0, 2, 0, 1]
n3 = [0, 0, 0, 1, 0, 0, 1]
n5 = [0, 0, 0, 0, 0, 1, 0]

dp = defaultdict(int)
dp[(0,0,0)] = 1
for i in range(n):
    ndp = defaultdict(int)
    for (k2, k3, k5), v in dp.items():
        for j in range(1, 7):
            nk2 = min(k2+n2[j], two)
            nk3 = min(k3+n3[j], three)
            nk5 = min(k5+n5[j], five)
            ndp[(nk2, nk3, nk5)] += v
    dp = ndp.copy()

print(dp[(two, three, five)]/pow(6,n))
