# https://atcoder.jp/contests/abc271/tasks/abc271_f
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
a = [list(map(int, input().split())) for _ in range(n)]
dp1 = [[None] * n for _ in range(n)]
dp2 = [[None] * n for _ in range(n)]


for i in range(n):
    for j in range(n-i):
        aij = a[i][j]
        dp1[i][j] = defaultdict(int)
        if i == 0 and j ==0:
            dp1[i][j][aij] = 1
            continue
        if j != 0:
            for k, v in list(dp1[i][j-1].items()):
                dp1[i][j][aij^k] += v
        if i != 0:
            for k, v in list(dp1[i-1][j].items()):
                dp1[i][j][aij^k] += v


for i in range(n):
    for j in range(n-i):
        aij = a[n-1-i][n-1-j]
        dp2[i][j] = defaultdict(int)
        if i == 0 and j ==0:
            dp2[i][j][aij] = 1
            continue
        if j != 0:
            for k, v in list(dp2[i][j-1].items()):
                dp2[i][j][aij^k] += v
        if i != 0:
            for k, v in list(dp2[i-1][j].items()):
                dp2[i][j][aij^k] += v

ret = 0
for i in range(n):
    j = n - 1 - i
    for k, v1 in dp1[i][j].items():
        v2 = dp2[n-1-i][n-1-j][k^a[i][j]]
        ret += v1 * v2

print(ret)
