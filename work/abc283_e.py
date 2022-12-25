# https://atcoder.jp/contests/abc283/tasks/abc283_e
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
n, m = map(int, input().split())
A = []
for _ in range(n):
    a = 0
    for i, ai in enumerate(list(map(int, input().split()))):
        a += ai << i
    A.append(a)


def isalone(j, B):
    # (1, j)
    i = 1
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if isinhw(ni, nj, 3, m):
            if B[ni] >> nj & 1 == B[i] >> j & 1:
                return False
    return True


def checkrow(u, v, w):
    # returns when determine a[i] , a[i-1] is ok or ng
    for j in range(m):
        if isalone(j, [u, v, w]):
            return False
    return True

if n == 2:
    ret = INF
    if checkrow(A[0], A[1], ~A[1]) and checkrow(~A[0], A[0], A[1]):
        ret = min(ret, 0)
    if checkrow(A[0], ~A[1], A[1]) and checkrow(~A[0], A[0], ~A[1]):
        ret = min(ret, 1)
    if checkrow(~A[0], A[1], ~A[1]) and checkrow(A[0], ~A[0], A[1]):
        ret = min(ret, 1)
    if checkrow(~A[0], ~A[1], A[1]) and checkrow(A[0], ~A[0], ~A[1]):
        ret = min(ret, 0)
    print(-1 if ret == INF else ret)
    exit()

dp = [[INF] * 2 for _ in range(2)]
if checkrow(~A[0], A[0], A[1]): dp[0][0] = 0
if checkrow(A[0], ~A[0], A[1]): dp[1][0] = 1
if checkrow(~A[0], A[0], ~A[1]): dp[0][1] = 1
if checkrow(A[0], ~A[0], ~A[1]): dp[0][0] = 2
#print(dp)
for i in range(1, n-1):
    ndp = [[INF] * 2 for _ in range(2)]
    au = [A[i-1], ~A[i-1]]
    av = [A[i], ~A[i]]
    aw = [A[i+1], ~A[i+1]]
    for u in range(2):
        for v in range(2):
            if dp[u][v] == INF: continue
            for w in range(2):
                if checkrow(au[u], av[v], aw[w]):
                    ndp[v][w] = min(ndp[v][w], dp[u][v] + w)
    dp = ndp
#    print(dp)
ret = INF
if checkrow(A[n-2], A[n-1], ~A[n-1]): ret = min(ret, dp[0][0])
if checkrow(A[n-2], ~A[n-1], A[n-1]): ret = min(ret, dp[0][1])
if checkrow(~A[n-2], A[n-1], ~A[n-1]): ret = min(ret, dp[1][0])
if checkrow(~A[n-2], ~A[n-1], A[n-1]): ret = min(ret, dp[1][1])
print(-1 if ret == INF else ret)
