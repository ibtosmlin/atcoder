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
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

able = set(["1", "2", "3", "4", "5"])
for i in range(h):
    for j in range(w):
        if c[i][j] != '.': continue
        use = set([])
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            di = i + dx
            dj = j + dy
            if not ((0<=di<h) and (0<=dj<w)): continue
            use.add(c[di][dj])
        c[i][j] = list((able - use))[0]
for ci in c:
    print(''.join(ci))
