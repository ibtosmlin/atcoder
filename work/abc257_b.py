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
n,k,q= map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

p = []
for ai in a:
    p.append(ai)
for li in l:
    li -= 1
    if p[li] == n:
        continue
    if li+1 < k:
        if p[li] +1 == p[li+1]:
            continue
    p[li] += 1

print(*p)