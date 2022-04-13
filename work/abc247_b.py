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

m = []
d = defaultdict(int)
for _ in range(n):
    a, b = input().split()
    m.append((a, b))
    d[a] += 1
    d[b] += 1

for i in range(n):
    a,b = m[i]
    if d[a] > 1 and d[b] > 1 and a!=b:
        end('No')
    elif a == b and d[a] > 2 and d[b] > 2:
        end('No')
end('Yes')