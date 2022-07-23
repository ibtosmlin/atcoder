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
n, m, s, t = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

seen = [-1] * n
hit = False
ret = []
def dfs(x, p=-1, d=0):
    global hit
    if x == t: hit = True
    for nx in edges[x]:
        if nx == p: continue
        if seen[nx] != -1: continue
        seen[nx] = d+1
        dfs(nx, x, d+1)
    if hit:
        ret.append(x)
dfs(s)
print(ret)