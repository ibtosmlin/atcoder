# https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1
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
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()

ls = list(input().split())
n = int(input())
mls = []
for _ in range(n):
    mls.append(input())

def isoks(s, t):
    if len(s) != len(t):
        return False
    for si, ti in zip(s, t):
        if ti != '*' and si != ti:
            return False
    return True

def isok(s):
    for t in mls:
        if isoks(s, t):
            return True
    return False

ret = []

for s in ls:
    if isok(s):
        ret.append('*'*len(s))
    else:
        ret.append(s)

print(' '.join(ret))
