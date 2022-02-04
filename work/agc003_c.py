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
n = int(input())

a0 = []
a1 = []
heapify(a0)
heapify(a1)

seq = []

for i in range(n):
    ai = int(input())
    seq.append(ai)
    if i%2:
        heappush(a1, ai)
    else:
        heappush(a0, ai)

seq.sort()
ret = 0
for i in range(n):
    if i%2==0:
        x = heappop(a0)
        if x != seq[i]:
            y = heappop(a1)
            ret += 1
            heappush(a1, x)
    else:
        x = heappop(a1)
        if x != seq[i]:
            y = heappop(a0)
            ret += 1
            heappush(a0, x)

print(ret)
