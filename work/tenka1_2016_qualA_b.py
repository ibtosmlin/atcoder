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
for c in range(n-1):
    c += 1
    p = int(input())
    edges[p].append(c)
    edges[c].append(p)

cost = [-1] * n
for _ in range(m):
    b, c = map(int, input().split())
    cost[b] = c

def dfs(x, p=-1):
    if cost[x] != -1: return cost[x]
    mn = INF
    for nx in edges[x]:
        if nx == p: continue
        if cost[nx] == -1:
            cost[nx] = dfs(nx, x)
        mn = min(mn, cost[nx])
    cost[x] = mn
    return mn

dfs(0)
cost[0] = 0
ret = 0
def dfs2(x, p=-1):
    global ret
    cx = cost[x]
    for nx in edges[x]:
        if nx == p: continue
        ret += cost[nx] - cx
        dfs2(nx, x)

dfs2(0)
print(ret)