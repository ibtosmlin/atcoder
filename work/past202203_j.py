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

class Combination:
    """nPr,nCr等の前計算

    Parameters
    ----------
    max_n : int, optional
        nの最大値, by default 1
    mod : int, optional
        modの値, by default 10**9+7

    Note:
    ----------
    n = 10**6 くらい
    """
    def __init__(self, max_n: int=1, mod : int=10**9+7) -> None:
        self.mod = mod
        self.max_n = 1
        self.factorial = [1, 1]
        self.inverse = [None, 1]
        self.f_inverse = [1, 1]
        self.__preprocessing(max_n)


    def __preprocessing(self, max_n:int) -> None:
        fac = self.factorial
        inv = self.inverse
        finv = self.f_inverse
        mod = self.mod
        fac += [-1] * (max_n - self.max_n)
        inv += [-1] * (max_n - self.max_n)
        finv += [-1] * (max_n - self.max_n)
        for i in range(self.max_n + 1, max_n + 1):
            fac[i] = fac[i - 1] * i % mod
            inv[i] = mod - inv[mod % i] * (mod // i) % mod
            finv[i] = finv[i - 1] * inv[i] % mod
        self.max_n = max_n


    def fac(self, n:int) -> int:
        """n!
        """
        if n < 0:
            return 0
        if n > self.max_n: self.__preprocessing(n)
        return self.factorial[n]


    def nCr(self, n:int, r:int) -> int:
        """nCr
        n個のものからr個選ぶ
        """
        if n < r or n < 0 or r < 0:
            return 0
        if n > self.max_n: self.__preprocessing(n)
        return self.factorial[n] * (self.f_inverse[r] * self.f_inverse[n - r] % self.mod) % self.mod


    def nPr(self, n:int, r:int) -> int:
        """nPr
        n個のものからr個選んで並べる
        """
        if n < r or n < 0 or r < 0:
            return 0
        if n > self.max_n: self.__preprocessing(n)
        return self.factorial[n] * self.f_inverse[n - r] % self.mod


    def nHr(self, n:int, r:int) -> int:
        """nHr = n-1+rCr
        n種類のものからr個重複を許して選ぶ(一個も選ばれないものがあっても可)
        (一個も選ばれないものがダメな場合はnをn-rとする・あらかじめ１個づつ選んでおく)
        """
        return self.nCr(n-1+r, n-1)


n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

cmb = Combination(n, mod1)

nCk = cmb.nCr(n, k)
invnCk = modinv(nCk, mod1)
ret = 0
for r in range(k-1, n):
    ret += cmb.nCr(r, k-1) * a[r] * invnCk
    ret %= mod1

for l in range(n-k+1):
    ret -= cmb.nCr(n-1-l, k-1) * a[l] * invnCk
    ret %= mod1

print(ret)