# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c
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
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = sum(a)
sb = sum(b)
if sa < sb: end(-1)
pos = []
neg = []
for ai, bi in zip(a, b):
    if ai - bi < 0:
        neg.append(bi - ai)
    else:
        pos.append(ai - bi)

pos.sort(reverse=True)
neg.sort(reverse=True)

posp = pos[:]


i = 0
j = 0
ret = 0
while j < len(neg):
    while neg[j] > 0:
        d = min(pos[i], neg[j])
        neg[j] -= d
        pos[i] -= d
        if pos[i] == 0:
            i += 1
    j += 1

ret = len(neg)
for p, q in zip(pos, posp):
    if p!=q:
        ret += 1

print(ret)