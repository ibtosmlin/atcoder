# https://atcoder.jp/contests/newjudge-2308-algorithm/tasks/abc260_f
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
s, t, m = map(int, input().split())
G = [[] for _ in range(s)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b-s)
for gi in G:
    gi.sort()


X = defaultdict(int)
for a in range(s):
    l = len(G[a])
    for i in range(l):
        u = G[a][i]
        for j in range(i+1, l):
            v = G[a][j]
            if u * s + v in X:
                b = X[u * s + v]
                print(a+1, b+1, u+1+s, v+1+s)
                exit()
            else:
                X[u*s+v] = a
print(-1)