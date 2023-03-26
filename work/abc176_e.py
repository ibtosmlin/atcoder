# https://atcoder.jp/contests/abc176/tasks/abc176_e
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
h, w, m = map(int, input().split())

cnth = [0] * h
cntw = [0] * w
cnt = []

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    cnth[u] += 1
    cntw[v] += 1
    cnt.append((u, v))

Mosth = set()
Mh = max(cnth)
for i in range(h):
    if cnth[i] == Mh:
        Mosth.add(i)

Mostw = set()
Mw = max(cntw)
for i in range(w):
    if cntw[i] == Mw:
        Mostw.add(i)

for u, v in cnt:
    if u in Mostw and

