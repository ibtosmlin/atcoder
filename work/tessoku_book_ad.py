# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ad
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


#####################################
# nCr % 10**9+7
#####################################
mod, lim = 10**9+7, 10**6                   # mod素数, 出力の制限
g1, g2 = [[1]*(lim+1) for _ in range(2)]    # ！と逆元tbl
for i in range(2, lim + 1):
    g1[i] = g1[i-1] * i % mod
g2[-1] = pow(g1[-1], mod-2, mod)
for i in range(lim, 0, -1):
    g2[i-1] = g2[i] * i % mod

def fac(n): return g1[n]
def facinv(n): return g2[n]
def nCr(n, r):
    """nCr
    n個のものからr個選ぶ
    """
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return fac(n) * facinv(r) * facinv(n-r) % mod

def nPr(n, r):
    """nPr
    n個のものからr個選んで並べる
    """
    if ( r<0 or r>n ):
        return 0
    return fac(n) * facinv(n-r) % mod

def nHr(n, r):
    """nHr = n-1+rCr
    n種類のものからr個重複を許して選ぶ(一個も選ばれないものがあっても可)
    (一個も選ばれないものがダメな場合はnをn-rとする・あらかじめ１個づつ選んでおく)
    """
    return nCr(n-1+r, n-1)

n, r = map(int, input().split())
ret = nCr(n, r)
print(ret)
