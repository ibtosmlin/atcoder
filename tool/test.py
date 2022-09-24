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
n, x = map(int, input().split())
s = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == '#':
            s[i][j] = 1
        else:
            s[i][j] = 0

for _ in range(x):
    ns = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cnt = 0
            for u, v in direc:
                ni = i + u
                nj = j + v
                if not isinhw(n, n, ni, nj): continue
                cnt += s[i][j]
            if s[i][j] == 0 and cnt == 3:
                ns[i][j] = 1
            elif s[i][j] == 1 and 2 <= cnt <= 3:
                ns[i][j] = 1
            else:
                ns[i][j] = 0
    s = ns.copy()

for i in range(n):
    ret = ''
    for j in range(n):
        if s[i][j] == 1:
            ret += '#'
        else:
            ret += '.'
    print(ret)
