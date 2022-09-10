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

from collections import deque


def _dfs(n, G, root=0, cost=1):
    _depth = [None] * n
    q = deque()
    q.append(root)
    _depth[root] = 0
    farest_dist = 0
    farest_node = 0
    _parent = [None] * n
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            if type(nxt) != int: nxt, cost = nxt
            if _depth[nxt] != None: continue
            q.append(nxt)
            newdep = dep + cost
            _depth[nxt] = newdep
            _parent[nxt] = cur
            if newdep > farest_dist:
                farest_dist = newdep
                farest_node = nxt
    return farest_node, farest_dist, _depth, _parent


def tree_diameter(n, G, cost=1):
    u, *_ = _dfs(n, G, 0)
    v, diam, depth, parent = _dfs(n, G, u)
    return u, v, diam, depth, parent


def tree_heights(n, G, cost=1):
    u, _, __ = _dfs(n, G, 0)
    v, _, depthu = _dfs(n, G, u)
    _, __, depthv = _dfs(n, G, v)
    return [max(x, y) for x, y in zip(depthu, depthv)]


##############################


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
#    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

u, v, x, __, parent = tree_diameter(n, G)

path = [v]
cur = v
while parent[cur] != None:
    cur = parent[cur]
    path.append(cur)
print(x, len(path))
print(*path[::-1])
