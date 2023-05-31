# https://atcoder.jp/contests/arc139/tasks/arc139_b
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
t = int(input())
def solv():
    n, a, b, x, y, z = map(int, input().split())
    if n == 0: return 0
    y = min(y, a*x)
    z = min(z, b*x)
    if y*b > z*a:
        y, z, a, b = z, y, b, a
    ret = float('inf')
    if n // a < a-1:
        for ca in range(n//a+1):
            l, cost = n, 0
            cost += ca * y
            l -= ca * a
            cb = l // b
            cost += cb * z
            l -= cb * b
            cost += l * x
            ret = min(ret, cost)
    else:
        for cb in range(a):
            l, cost = n, 0
            cost += cb * z
            l -= cb * b
            ca = l // a
            cost += ca * y
            l -= ca * a
            cost += l * x
            ret = min(ret, cost)
    return ret

for _ in range(t):
    print(solv())