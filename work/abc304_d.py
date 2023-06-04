# https://atcoder.jp/contests/abc304/tasks/abc304_d
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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()

from bisect import bisect_left, bisect_right
w, h = map(int, input().split())
n = int(input())

point = []
for i in range(n):
    p, q = map(int, input().split())
    point.append((p, q))

a = int(input())
A = list(map(int, input().split())) + [w]
b = int(input())
B = list(map(int, input().split())) + [h]

d = defaultdict(int)
for p,q in point:
    d[(bisect_right(A, p), bisect_right(B, q))] += 1

x = d.values()
m = min(x)
M = max(x)
if len(x) != (a+1)*(b+1):
    m = 0
print(m, M)
