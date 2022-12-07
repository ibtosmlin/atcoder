# https://atcoder.jp/contests/wupc2012/tasks/wupc2012_3
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
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]# + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        x = g[i][j]
        if x == 'S':
            st0 = (i, j)
            g[i][j] = '.'
        if x == 'G':
            st1 = (i, j)
            g[i][j] = '.'
INF = 10**9

def bfs(st, g):
    ret = [[INF] * m for _ in range(n)]
    que = deque([])
    que.append(st)
    ret[st[0]][st[1]] = 0
    while que:
        i, j = que.popleft()
        d = ret[i][j]
        for di, dj in direc:
            ni, nj = i + di, j + dj
            if not isinhw(ni, nj, n, m): continue
            if g[ni][nj] == '#': continue
            if ret[ni][nj] != INF: continue
            if g[ni][nj] == 'C':
                return d + 1
            que.append((ni, nj))
            ret[ni][nj] = d + 1
    return - float('inf')

ret = bfs(st1, g)+bfs(st0, g)
print(-1 if ret == -float('inf') else ret)