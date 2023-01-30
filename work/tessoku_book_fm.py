# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fm
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()
n = int(input())
k = int(input())
mtgs = []
for i in range(n):
    l, r = map(int, input().split())
    r += k
    mtgs.append((l, r, i))

mtgs.sort(key= lambda x: x[1])
f = defaultdict(int)
now = 0
cnt = 0
for l, r, _ in mtgs:
    if l >= now:
        cnt += 1
        now = r
        f[now] = cnt

mtgs.sort(key= lambda x: x[0])
g = defaultdict(int)
now = 86400*2
cnt = 0
for l, r, _ in mtgs[::-1]:
    if r <= now:
        cnt += 1
        now = l
        g[now] = cnt

f[0] = 0
g[86400*2] = 0

fky = list(f.keys())
gky = list(g.keys())
fky.sort()
gky.sort()

from bisect import bisect_left, bisect_right
mtgs.sort(key= lambda x: x[2])

for l, r, _ in mtgs:
    x = f[fky[bisect_right(fky, l)]]
    y = g[gky[bisect_left(gky, r)]]
    print(x + y)
#print(f, fky)
#print(g, gky)