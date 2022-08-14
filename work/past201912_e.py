import enum
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
n, q = map(int, input().split())
ret = [['N'] * n for _ in range(n)]
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        a, b = que[1:]
        a -= 1; b -= 1
        ret[a][b] = 'Y'
    elif que[0] == 2:
        a = que[1]
        a -= 1
        up = set()
        for b in range(n):
            if ret[b][a] == 'Y':
                up.add(b)
        for x in up:
            ret[a][x] = 'Y'
    else:
        a = que[1]
        a -= 1
        up = set()
        for x in range(n):
            if ret[a][x] == 'Y':
                for c in range(n):
                    if c == a: continue
                    if ret[x][c]== 'Y':
                        up.add(c)
        for x in up:
            ret[a][x] = 'Y'
for reti in ret:
    print(''.join(reti))