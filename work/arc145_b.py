import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
from types import MappingProxyType
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
N, a, b = map(int, input().split())


# a>bの時
# n%a<b n>=aなら勝てる
# 1<=n<=b-1  負ける



if a <= b:
# a<=bの時
# n>=aの時必ず勝てる
# 1<=n<=a-1の時負ける
    end(max(N-(a-1),0))

else:
    N -= a
    if N < 0: end(0)
    t, r = divmod(N, a)
    ret = t * b
    ret += min(r+1, b)
    end(ret)
