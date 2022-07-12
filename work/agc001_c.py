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
n, k = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)


def bfs(xs):
    seen = [-1] * n
    q = deque([])
    for x in xs:
        seen[x] = 0
        q.append((x, 0))
    while q:
        x, d = q.popleft()
        for nx in edges[x]:
            if seen[nx] != -1: continue
            seen[nx] = d+1
            q.append((nx, d+1))
    cnt = 0
    for si in seen:
        if si > k//2: cnt += 1
    return cnt

if k % 2 == 0:
    ret = INF
    for i in range(n):
        nw = bfs([i])
        ret = min(ret, nw)
else:
    ret = INF
    for i in range(n):
        for j in edges[i]:
            nw = bfs([i, j])
            ret = min(ret, nw)

print(ret)