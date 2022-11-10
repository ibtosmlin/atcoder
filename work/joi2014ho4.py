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

n, m, x = map(int, input().split())
h = [int(input()) for _ in range(n)]
G = [[] for _ in range(m)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    if h[a] >= w:
        G[a].append((b, w))
    if h[b] >= w:
        G[b].append((a, w))

dist = [INF] * n
dist[0] = 0
q = heapify([(0, 0)])
while q:
    c, x = heappop(q)
    if dist[x] < c: continue
    for nx, nc in G[x]:
        nxt = c + nc
        