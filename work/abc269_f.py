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
q = int(input())


def tousa(f, d, c):
    ret = (f + f + d * (c-1)) * c // 2
    return ret % mod1


def grid(x, y):
    if x == 0 or y == 0: return 0
    # 横集計
    # 一行目の数字の個数fc
    fc = (y+1) // 2
    first = tousa(1, 2, fc)
    # 二行目の数字の個数sc
    sc = y // 2
    second = tousa(m+2, 2, sc)

    # 縦集計
    # 奇数行
    oddd = 2 * m * fc
    oddc = (x+1) // 2
    total = tousa(first, oddd, oddc)
    # 偶数行
    evend = 2 * m * sc
    evenc = x // 2
    total += tousa(second, evend, evenc)
    return total % mod1


def total(a, b, c, d):
    a -= 1; c -= 1
    ret = 0
    ret += grid(b, d)
    ret -= grid(b, c)
    ret -= grid(a, d)
    ret += grid(a, c)
    return ret % mod1


for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(total(a, b, c, d))