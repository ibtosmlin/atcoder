# https://atcoder.jp/contests/abc287/tasks/abc287_c
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()
from collections import deque

def _bfs(n, G, root=0):
    _depth = [None] * n
    q = deque()
    q.append(root)
    _depth[root] = 0
    _parent = [None] * n
    farest_dist = 0
    farest_node = 0
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            nx, cost = nxt
            if _depth[nx] != None: continue
            q.append(nx)
            newdep = dep + cost
            _depth[nx] = newdep
            if newdep > farest_dist:
                farest_dist = newdep
                farest_node = nx
    return farest_node, farest_dist, _depth, _parent


def tree_diameter(n, G):
    u, *_ = _bfs(n, G, 0)
    v, diam, depth, parent = _bfs(n, G, u)
    return u, v, diam, depth, parent


def tree_heights(n, G):
    u, *_ = _bfs(n, G, 0)
    v, _, depthu, _ = _bfs(n, G, u)
    _, __, depthv, __ = _bfs(n, G, v)
    return [max(x, y) for x, y in zip(depthu, depthv)]


##############################

n, m = map(int, input().split())
if m != n-1:
    end('No')
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int1, input().split())
    G[a].append((b, 1))
    G[b].append((a, 1))

if tree_diameter(n, G)[2] == n-1:
    print('Yes')
else:
    print('No')
