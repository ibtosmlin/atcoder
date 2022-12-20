# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ff
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
nums = [input().split() for _ in range(n)]

def checkxy(x, y, p):
    cnt = 0
    for xi, yi in zip(x, y):
        if xi != yi:
            cnt += 1
    if p == '1':
        return cnt == 0
    if p == '2':
        return cnt == 1
    if p == '3':
        return cnt > 1

def check(x):
    for y, p in nums:
        if not checkxy(x, y, p):
            return False
    return True

ret = []
for x in range(10000):
    x = str(x).zfill(4)
    if check(x):
        ret.append(x)

if len(ret) > 1:
    print("Can't Solve")
else:
    print(*ret)