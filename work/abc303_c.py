# https://atcoder.jp/contests/abc303/tasks/abc303_c
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
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m, h, k = map(int, input().split())
s = input()
pt = set(tuple(map(int, input().split())) for _ in range(m))
x, y = 0, 0
move = 0
for si in s:
    move += 1
    if si == 'R':
        x += 1
    elif si == 'L':
        x -= 1
    elif si == 'U':
        y += 1
    else:
        y -= 1
    h -= 1
    if h < 0:
        no()
        exit()
    if (x, y) in pt:
        if h < k:
            h = k
            pt.remove((x, y))
yes()
exit()
