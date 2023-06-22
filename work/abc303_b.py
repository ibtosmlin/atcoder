# https://atcoder.jp/contests/abc303/tasks/abc303_b
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
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
n, m = map(int, input().split())
a = [list(map(int1, input().split())) for _ in range(m)]

fri = set()
for i in range(m):
    for j in range(n-1):
        u = a[i][j]
        v = a[i][j+1]
        if u > v:
            u, v = v, u
        fri.add((u, v))

ret = 0
for i in range(n):
    for j in range(i):
        if (j, i) in fri: continue
        ret += 1
print(ret)
