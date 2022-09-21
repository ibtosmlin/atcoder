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
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])

n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]
seen = [False] * n

direc = [(-1, -1),(-1, 0),(0,-1),(0,1),(1,0),(1,1)]

def bfs(x):
    seen[x] = True
    que = deque([point[x]])
    while que:
        u, v = que.popleft()
        for du, dv in direc:
            nu = u + du
            nv = v + dv
            if (nu, nv) in point:
                i = point.index((nu, nv))
                if seen[i] == True: continue
                que.append((nu, nv))
                seen[i] = True

ret = 0
for i in range(n):
    if seen[i]: continue
    ret += 1
    bfs(i)

print(ret)