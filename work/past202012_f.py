import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
from xml.etree.ElementTree import QName
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
n, m = map(int, input().split())
bombs = set()
for _ in range(m):
    a, b, c = map(int1, input().split())
    bomb = (1<<a) | (1<<b) | (1<<c)
    bombs.add(bomb)

ret = 0
for j in range(1<<n):
    fg = True
    u = set()
    for b in bombs:
        x = bin(j&b).count('1')
        if x == 3:
            fg = False
        if x == 2:
            u.add(b ^ (j&b))
    if fg:
        cnt = len(u)
        if ret < cnt:
            ret = cnt

print(ret)
