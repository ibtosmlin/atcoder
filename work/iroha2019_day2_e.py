# https://atcoder.jp/contests/iroha2019-day2/tasks/iroha2019_day2_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

mod = 1000000007
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

cmb = Combination
n, m = map(int, input().split())
total = cmb.nCr(n+m, m)

if n == m:
    ret1 = 2
    ret2 = 
