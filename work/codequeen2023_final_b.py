# https://atcoder.jp/contests/codequeen2023-final-open/tasks/codequeen2023_final_b
from itertools import *
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys; sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i, base='a'): return chr(ord(base) + i%26)    # i=0->'a', i=25->'z'
def alpind(a, base='a'): return ord(a)-ord(base)
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): exit(print(r))

n = int(input())
R = set()
C = set()
X = set()
Y = set()

for _ in range(n-1):
    r, c = map(int, input().split())
    R.add(r)
    C.add(c)
    X.add(r+c)
    Y.add(r-c)

for r in range(1,n+1):
    if r in R: continue
    for c in range(1, n+1):
        if c in C: continue
        if r+c in X: continue
        if r-c in Y: continue
        exit(print(r, c))
exit(print(-1))
