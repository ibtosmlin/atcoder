# https://atcoder.jp/contests/past202209-open/tasks/past202209_f
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
n = int(input())
A = list(map(int, input().split()))
X = []
for _ in range(n):
    c = int(input())
    cl = set(map(int, input().split()))
    X.append(cl)

q = int(input())
for _ in range(q):
    d = int(input())
    yl = set(map(int, input().split()))
    ret = -1
    mvl = -1
    for i, (a, x) in enumerate(zip(A, X)):
        if len(x & yl) > 0: continue
        if a > mvl:
            mvl = a
            ret = i+1
    print(ret)




