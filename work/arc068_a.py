# https://atcoder.jp/contests/abc053/tasks/arc068_a
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
x = int(input())
ret = 2 * (x//11)
x %= 11
if x == 0:
    end(ret)
if x == 1:
    end(ret + 1)
if x == 2:
    end(ret + 1)
if x == 3:
    end(ret + 1)
if x == 4:
    end(ret + 1)
if x == 5:
    end(ret + 1)
if x == 6:
    end(ret + 1)
if x == 7:
    end(ret + 2)
if x == 8:
    end(ret + 2)
if x == 9:
    end(ret + 2)
if x == 10:
    end(ret + 2)

