# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p
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
dp = [INF] * n
dp[0] = 0
for i in range(n):
    nw = dp[i]
    if i+1 < n:
        dp[i+1] = min(dp[i+1], nw + a[i])
    if i+2 < n:
        dp[i+2] = min(dp[i+2], nw + b[i])

ret = [n]
nw = n-1
while nw != 0:
    if dp[nw] == dp[nw-1] + a[nw-1]:
        nw = nw - 1
    else:
        nw = nw - 2
    ret.append(nw+1)

print(len(ret))
print(*ret[::-1])
