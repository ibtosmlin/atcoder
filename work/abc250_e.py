from bisect import bisect_left, bisect_right
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
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dica = dict()
a = [0] * n
b = [INF] * n

cnt = -1
for i, ai in enumerate(A):
    if not ai in dica:
        dica[ai] = cnt
        cnt += 1
    a[i] = cnt

for i, bi in enumerate(B):
    if not bi in dica: continue
    b[i] = dica[bi]

blen = [0] * n
bmax = [None] * n

nowset = set()
nowmax = -INF
nowlen = -1

for i, bi in enumerate(b):
    if not bi in nowset:
        nowset.add(bi)
        nowmax = max(nowmax, bi)
        nowlen += 1
    bmax[i] = nowmax
    blen[i] = nowlen

q = int(input())
for _ in range(q):
    x, y = map(int1, input().split())
    if a[x] == blen[y] and a[x] == bmax[y]:
        print('Yes')
    else:
        print('No')
