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
n, m = map(int, input().split())
s = []
d = defaultdict(int)
mx = 0
minb = INF
for i in range(n):
    a, b = map(int1, input().split())
    mx = max(mx, a)
    d[a] = max(d[a], b)
    minb = min(b, minb)
s.append((a, b))

ret = [0] * (m+10)

for l in range(minb+1):
    ret[mx-l] += 1
    ret[m-l] -= 1
    mx = max(d[l], mx)
    if mx<l: break

ret = list(accumulate(ret))
print(*ret[:m])
