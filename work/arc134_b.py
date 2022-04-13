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
s = list(input())
t = s[:]

a = [(i, si) for i, si in enumerate(s)][::-1]
a.sort(key=itemgetter(1))



l = -1
r = n

for p in range(n):
    for i, si in a:
        if not (l < i < r): continue
        r = i
        while l < r and s[l] <= si:
            l += 1
        if l>=r: break
        t[l], t[r] = s[r], s[l]
        l += 1
        if l>=r: break


print("".join(t))