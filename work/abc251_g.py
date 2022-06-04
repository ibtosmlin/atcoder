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
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int1, input().split())
    _a -=1
    _b -=1
    edges[_a].append(_b)
    edges[_b].append(_a)


t1 = []
q = deque([])
seen = [False] * n
q.append(0)
seen[0] = True
while q:
    nw = q.popleft()
    for nx in edges[nw]:
        if seen[nx]: continue
        q.appden(nx)
        seen[nx] = True
        t1.append((nw+1, nx+1))
print(t1)