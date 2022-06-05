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
n, k = map(int, input().split())
a = list(map(int, input().split()))

ret = [[] for _ in range(k)]
for i, ai in enumerate(a):
    ret[i%k].append(ai)

for i in range(k):
    ret[i].sort()

reta = []

for i in range(n):
    reta.append(ret[i%k][i//k])

a.sort()

if a == reta:
    print('Yes')
else:
    print('No')
