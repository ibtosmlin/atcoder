# https://atcoder.jp/contests/abc277/tasks/abc277_g
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

n, m, k = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)
C = list(map(int, input().split()))
invs = []
for i in range(n):
    u = len(G[i])
    invs.append(modinv(2*u, mod1))


N = n * (k+2)
off = n
dp = [-1] * N
dp[0] = 0
print(N, n, k)

for _ in range(k):
    ndp = [0] * N
    for i in range(N):
        mon = dp[i]
        if mon == -1: continue
        l = i // off
        v = i % off
        for nv in G[v]:
            if C[nv] == 1:
                print(l*off+nv+off, nv, l+1)
                ndp[l*off+nv+off] += mon * invs[v]
            else:
                ndp[l*off+nv] += ((l**2) + mon) * invs[v]
    for i in range(N):
        dp[i] = ndp[i]%mod1

print(sum(dp)%mod1)
