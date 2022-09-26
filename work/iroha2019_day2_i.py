# https://atcoder.jp/contests/iroha2019-day2/tasks/iroha2019_day2_i
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

##########################################

h, w, x = map(int, input().split())
s = tuple(map(int1, input().split()))
g = tuple(map(int1, input().split()))
G = [list(map(int, input().split())) for _ in range(h)]
C = [0] + list(map(int, input().split()))

seen = [[-1] * w for _ in range(h)]
edges = [[] for _ in range(h*w)]

def dfs(u, nodeid):
    x, y = u
    seen[x][y] = nodeid
    mtid = G[x][y]
    for dx, dy in direc:
        nx = x + dx
        ny = y + dy
        if not isinhw(nx, ny, h, w): continue
        if seen[nx][ny] != -1:
            edges.append([seen[nx][ny], nodeid, G[nx][ny]])
            .add((, nodeid))
            continue
        if G[nx][ny] == mtid:
            dfs((nx, ny), nodeid)



dfs(s, 0)
if seen[g[0]][g[1]] == 0:
    end(0)
dfs(g, h*w-1)

nodeid = 0
for i in range(h):
    for j in range(w):
        if seen[i][j] != -1: continue
        nodeid += 1
        dfs((i, j), nodeid)
