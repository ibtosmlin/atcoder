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

n, m, x = map(int, input().split())
T = [int1(input()) for _ in range(n)]

edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    a -= 1; b -= 1
    edges[a].append((b, d))
    edges[b].append((a, d))

dist = [[INF] * (2*x + 1) for _ in range(n)]
q = []
heapify(q)
dist[0][0] = 0
heappush(q, (0, 0, -x))  # dist, node, t
while q:
    d, node, t = heappop(q)
    if dist[node][t+x] < d: continue
    for nnode, ncost in edges[node]:
        nd = d + ncost
        if T[nnode] == 1 and t < 0 and t + ncost < 0: continue
        if T[nnode] == -1 and t > 0 and t - ncost > 0: continue
        if T[nnode] == -1:
            nt = -x
        if T[nnode] == 1:
            nt = x
        if T[nnode] == 0:
            if t < 0:
                nt = min(0, t + ncost)
            elif t > 0:
                nt = max(0, t - ncost)
            else:
                nt = t
        if dist[nnode][nt+x] <= nd: continue
        dist[nnode][nt+x] = nd
        heappush(q, (nd, nnode, nt))

print(min(dist[n-1]))
