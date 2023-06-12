# https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_b
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
n, k = map(int, input().split())

bit = [0] * (n+2)
fg = 0
for _ in range(k):
    x = int(input())
    if x == 0:
        fg = 1
    bit[x] += 1
for i in range(1, n+2):
    bit[i] += bit[i-1]

def isok(d, fg):
    for l in range(1, n+1-d):
        cnt = d - (bit[l+d] - bit[l])
        if cnt <= fg:
            return True
    return False

ok = 0
ng = n+1
while ng-ok > 1:
    mid = (ng+ok) // 2
    if isok(mid, fg):
        ok = mid
    else:
        ng = mid

print(ok)