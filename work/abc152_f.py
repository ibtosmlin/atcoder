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
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)
m = int(input())
cond = [tuple(map(int1, input().split())) for _ in range(m)]

conde = []

def dfs(f, t):
    que = deque()
    seen = [False] * n
    parent = [-1] * n
    que.append(f)
    seen[f] = True
    while que:
        x = que.pop()
        for nx in G[x]:
            if seen[nx]: continue
            parent[nx] = x
            if nx == t:
                return parent
            seen[nx] = True
            que.append(nx)

for u, v in cond:
    parent = dfs(u, v)
    nw = v
    nv = parent[nw]
    eds = set()
    while nv != -1:
        eds.add(min(nw*10**5 + nv, nw + nv*10**5))
        nw = nv
        nv = parent[nw]
    conde.append(eds)


total = 0
for i in range(1<<m):
    used = set()
    bitc = 0
    for j in range(m):
        if i >> j & 1:
            used |= conde[j]
            bitc += 1
    cnt = 1 << n-1-len(used)
    bitc %= 2
    if bitc:
        total -= cnt
    else:
        total += cnt

print(total)