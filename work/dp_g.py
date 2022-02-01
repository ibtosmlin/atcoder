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

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
indeg = [0] * n
for _ in range(m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    indeg[_b] += 1


def bfs():
    que = deque()
    lng = [-1] * n
    for i in range(n):
        if indeg[i] != 0: continue
        que.append(i)
        lng[i] = 0
    while que:
        c = que.popleft()
        for nx in edges[c]:
            if lng[nx] != -1:continue
            lng[nx] = lng[c] + 1
            que.append(nx)
    return max(lng)




print(bfs())
