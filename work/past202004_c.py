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
g = [list(input()) for _ in range(n)]
w = 2*n - 1

def isX(i, j):
    for dj in [-1, 0, 1]:
        if 0<= j + dj < w and g[i+1][j+dj] == 'X':
            return True
    return False


for i in range(n-1)[::-1]:
    for j in range(w):
        if g[i][j] != '#': continue
        if isX(i, j):
            g[i][j] = 'X'

for gi in g:
    print(''.join(gi))
