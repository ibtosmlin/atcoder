# https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho4
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


##########################################

n, m, x = map(int, input().split())
H = [int(input()) for _ in range(n)]
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((b,c))
    G[b].append((a,c))

dist = [INF] * n
que = [(0, 0)]
heapify(que)
while que:
    time, x = heappop(que)
    if dist[x] < time: continue
    for nx, nd in G[x]:
        nhx =  + nd
        ntime = hx + nd
        ad = max(0, nhx - H[nx])
        nhx += ad
        ntime += ad
        if dist.get((nx, nhx), INF) <= ntime: continue
        dist[(nx, nhx)] = ntime
        if nx == 0: continue
        heappush(que, (ntime, nx, nhx))

print(dist)
