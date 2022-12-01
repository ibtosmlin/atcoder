# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bk
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

n, m = map(int, input().split())
ret = [INF] * n
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)

que = deque()
que.append(0)
ret[0] = 0
while que:
    x = que.popleft()
    for nx in G[x]:
        if ret[nx] != INF: continue
        ret[nx] = ret[x] + 1
        que.append(nx)
for ri in ret:
    if ri == INF:
        ri = 120
    print(ri)
