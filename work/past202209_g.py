# https://atcoder.jp/contests/past202209-open/tasks/past202209_g
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
def fstr(x): return f'{x:.10f}'

from itertools import combinations
n, l, k = map(int, input().split())
ss = [list(input()) for _ in range(n)]

ret = 0
for cmb in combinations(range(l), l-k):
    sts = []
    for si in ss:
        sts.append(''.join([si[i] for i in cmb]))
    sts = Counter(sts)
    ret = max(ret, max(list(sts.values())))
print(ret)