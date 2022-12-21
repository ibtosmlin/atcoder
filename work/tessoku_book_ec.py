# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ec
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
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd

class RollingHash():
    def __init__(self, s:str, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)
        self.length = l = len(s)
        self.h = h = [0]*(l+1)

        v, t = 0, 1
        for i in range(l):
            v, t = v * base, t * base
            v += ord(s[i])
            v, t = v % mod, t % mod
            h[i+1], pw[i+1] = v, t

    def get(self, l, r):
        # returns hashvalue of [l, r]
        if l > r: return False
        r = min(self.length, r)
        return (self.h[r] - self.h[l-1] * self.pw[r-l+1]) % self.mod

base = 31; mod = 10**9+7
n, q = map(int, input().split())
S = input()
RHS = RollingHash(S, base, mod)
RHT = RollingHash(S[::-1], base, mod)

for _ in range(q):
    l, r = map(int, input().split())
    hash1 = RHS.get(l, r)
    hash2 = RHT.get(n-r+1, n-l+1)

    if hash1 == hash2:
        print('Yes')
    else:
        print('No')
