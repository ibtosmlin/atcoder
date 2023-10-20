import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10001000)
import sys; input: lambda _: sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
s = input()
cnt = [0] * 26
for si in s:
    cnt[ord(si)-ord('a')] += 1

class Combination:
    def __init__(self, maxn:int=10**6, mod:int=1000000007) -> None:
        self.mod = mod
        self.maxn = maxn
        _maxn = maxn + 1
        fac, facinv, inv = [1]*_maxn, [1]*_maxn, [1]*_maxn
        for i in range(2, _maxn):
            fac[i] = fac[i-1] * i % mod
            inv[i] = _inv = (mod - inv[mod % i] * (mod // i) % mod) % mod
            facinv[i] = facinv[i-1] * _inv % mod
        self.fac = fac; self.facinv = facinv

    def nCr(self, n, r):
        """nCr
        n個のものからr個選ぶ
        """
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return self.fac[n] * (self.facinv[r] * self.facinv[n-r] % self.mod) % self.mod

mod = 998244353
cmb = Combination(5000, mod)
# cmb.nCr(n, j)

dp = [[0] * 5010 for _ in range(27)]
dp[0][0] = 1
for i, c in enumerate(cnt):
    for j in range(5001):
        for k in range(c+1):
            if j+k > 5000: break
            dp[i+1][j+k] += dp[i][j] * cmb.nCr(j+k, k)
            dp[i+1][j+k] %= mod
print((sum(dp[-1][1:]))%mod)
