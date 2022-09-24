# https://atcoder.jp/contests/agc058/tasks/agc058_a
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
p = list(map(int, input().split()))

k = 0
ret = []

def ope(i):
    global k, p, ret
    k += 1
    ret.append(i+1)
    p[i], p[i+1] = p[i+1], p[i]



if p[0] > p[1]: ope(0)

for i in range(0, 2*n, 2):
    if i+3 >= 2 * n: break
    p1, p2, p3 = p[i+1:i+4]
    # p[i+1], p[i+2], p[i+3]  => p[i+1] > p[i+2] < p[i+3] としたい

    # (p[i] < ) p[i+1] < p[i+2] < p[i+3]  => switch i+1, i+2
    if p1 < p2 < p3: ope(i+1)
    # (p[i] < ) p[i+1] < p[i+2] > p[i+3]  =>
                        # p[i+1] > p[i+3] => switch i+2, i+3
                        # p[i+1] < p[i+3] => switch i+1, i+2
    elif p1 < p2 > p3:
        if p1 > p3: ope(i+2)
        else: ope(i+1)
    # (p[i] < ) p[i+1] > p[i+2] > p[i+3]  => switch i+2, i+3
    elif p1 > p2 > p3: ope(i+2)
    # (p[i] < ) p[i+1] > p[i+2] < p[i+3]  => nop
    else:
        pass
print(k)
print(*ret)