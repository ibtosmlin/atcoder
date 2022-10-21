# https://atcoder.jp/contests/abc273/tasks/abc273_d
import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
from bisect import *
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
h, w, rs, cs = map(int, input().split())
rs -= 1
cs -= 1
n = int(input())
dicH = defaultdict(list)
dicW = defaultdict(list)
for _ in range(n):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    dicH[c].append(r)
    dicW[r].append(c)
for v in dicH.values():
    v.append(-1)
    v.append(h)
    v.sort()
for v in dicW.values():
    v.append(-1)
    v.append(w)
    v.sort()


q = int(input())
for _ in range(q):
    d, l = input().split()
    l = int(l)
    if cs not in dicH:
        dicH[cs] = [-1, h]
    if rs not in dicW:
        dicW[rs] = [-1, w]

    if d == 'D':
        u = bisect(dicH[cs], rs)
        rn = dicH[cs][u] - 1
        rs = min(rn, rs+l)
    if d == 'U':
        u = bisect(dicH[cs], rs) - 1
        rn = dicH[cs][u] + 1
        rs = max(rn, rs-l)

    if d == 'R':
        u = bisect(dicW[rs], cs)
        cn = dicW[rs][u] - 1
        cs = min(cn, cs+l)
    if d == 'L':
        u = bisect(dicW[rs], cs) - 1
        cn = dicW[rs][u] + 1
        cs = max(cn, cs-l)

    print(rs+1, cs+1)
