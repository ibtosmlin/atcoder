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

w = int(input())
m1 = set()
m2 = set()
gen = [False] * (w+1)

i = 1
while i <=w:
    if gen[i]:
        i += 1
        continue
    gen[i] = True
    nxti = i
    for j in m2:
        if i+j <= w:
            gen[i+j] = True
    for j in m1:
        if i+j <= w:
            nxti = max(i+j, nxti)
            gen[i+j] = True
            m2.add(i+j)
    m1.add(i)
    i = nxti + 1

print(len(m1))
print(*list(m1))