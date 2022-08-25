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
h, w = map(int, input().split())
g = [input() for _ in range(h)]
seen = [[False] * w for _ in range(h)]

x, y = 0, 0
while True:
    cx, cy = x, y
    seen[cx][cy] = True
    if g[cx][cy] == 'U': x -= 1
    if g[cx][cy] == 'D': x += 1
    if g[cx][cy] == 'L': y -= 1
    if g[cx][cy] == 'R': y += 1
    if not isinhw(x, y, h, w):
        print(cx+1, cy+1)
        exit()
    if seen[x][y]:
        print(-1)
        exit()
