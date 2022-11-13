# https://atcoder.jp/contests/abc277/tasks/abc277_e
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
n, m, k = map(int, input().split())

G = [[] for _ in range(n*2)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    if w == 1:
        G[a].append((b, 1))
        G[b].append((a, 1))
    else:
        G[a+n].append((b+n, 1))
        G[b+n].append((a+n, 1))

s = list(map(int1, input().split()))

for si in s:
    G[si].append((n+si, 0))
    G[n+si].append((si, 0))

INF = 10**9
dist = [INF] * (n*2)
deq = deque([])
deq.append(0)
dist[0] = 0
while deq:
    x = deq.popleft()
    for nx, cost in G[x]:
        d = dist[x] + cost
        if d < dist[nx]:
            dist[nx] = d
            if cost == 0:
                deq.appendleft(nx)
            else:
                deq.append(nx)
ret = min(dist[n-1], dist[2*n-1])
print(-1 if ret == INF else ret)