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
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])

################

n, m = map(int, input().split())
A = list(map(int, input().split()))
costs = [0] * n
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)
    costs[_a] += A[_b]
    costs[_b] += A[_a]

p = []
heapify(p)
for i, pi in enumerate(costs):
    heappush(p, (pi, i))

ret = 0
seen = set()

while p:
    pi, i = heappop(p)
    if i in seen: continue
    seen.add(i)
    ret = max(ret, pi)
    for j in edges[i]:
        if j in seen: continue
        costs[j] -= A[i]
        heappush(p, (costs[j], j))

print(ret)