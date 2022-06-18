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

n, m = map(int, input().split())
s = list(map(int, input().split()))
x = list(map(int, input().split()))

a = [0]
for si in s:
    a.append(si - a[-1])

var = []
for i in range(n):
    for xi in x:
        if i%2:
            var[i].append(xi - a[i])
        else:
            var[i].append(a[i] - xi)
var = set(var)

ret = 0
for f in var:
    f+ai* for i, ai in enumerate(a)]




print(max(cont.values()))