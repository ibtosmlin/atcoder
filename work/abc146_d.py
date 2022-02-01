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
n = int(input())
edgel = []
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int1, input().split())
    edges[a].append(b)
    edges[b].append(a)
    edgel.append((a, b))
d = dict()

def dfs(c, p, col):
    if len(edges[c]) == 0:
        return
    ncol = 0
    for nxt in edges[c]:
        if nxt==p: continue
        if nxt < c:
            nxt, c = c, nxt
        ncol += 1
        if ncol == col:
            ncol += 1
        d[(c, nxt)] = ncol
        dfs(nxt, c, ncol)

dfs(0, -1, 0)

print(max(d.values()))
for x in edgel:
    print(d[x])








#print('\n'.join(map(str, ret)))