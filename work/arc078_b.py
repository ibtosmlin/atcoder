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
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

def bfs(x):
    depth = [-1] * n
    que = deque([])
    que.append(x)
    depth[x] = 0
    while que:
        u = que.popleft()
        for v in edges[u]:
            if depth[v] != -1:
                continue
            depth[v] = depth[u] + 1
            que.append(v)
    return depth

d0 = bfs(0)
dn = bfs(n-1)

F = 0
for i in range(n):
    if d0[i] <= dn[i]:
        F += 1
S = n - F
if F>S:
    print('Fennec')
else:
    print('Snuke')
