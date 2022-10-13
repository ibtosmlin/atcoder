# https://atcoder.jp/contests/joi2016ho/tasks/joi2016ho_c
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
n, m, q = map(int, input().split())
edges = []
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int1, input().split())
    edges.append([a, b, INF])

for i in range(q):
    r = int1(input())
    edges[r][-1] = i+1

for a, b, w in edges:
    G[a].append((b, w))
    G[b].append((a, w))

seen = [-1] * n
que = deque([0])
seen[0] = 0
while que:
    x = que.popleft()
    for nx, _ in G[x]:
        if seen[nx] != -1: continue
        seen[nx] = seen[x] + 1
        que.append(nx)

parents = [[] for _ in range(n)]
parents[0] = [(-1, INF)]
for x in range(1, n):
    for nx, nw in G[x]:
        if seen[x] == seen[nx] + 1:
            parents[x].append((nx, nw))

stop = [-1] * n
stop[0] = INF
def dfs(x):
    if stop[x] != -1: return stop[x]
    ret = 0
    for px, sp in parents[x]:
        ret = max(ret, min(sp, dfs(px)))
    stop[x] = ret
    return ret

for i in range(1, n):
    dfs(i)

cnt = [0] * (1+q)
for i in range(1, n):
    if stop[i] == INF: continue
    cnt[stop[i]] += 1

cnt = list(accumulate(cnt))
for ci in cnt[1:]:
    print(ci)
