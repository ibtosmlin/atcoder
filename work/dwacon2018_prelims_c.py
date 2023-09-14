# https://atcoder.jp/contests/dwacon2018-prelims/tasks/dwacon2018_prelims_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1



#####################################
# nCr % 10**9+7
# http://zakii.la.coocan.jp/enumeration/10_balls_boxes.htm
#####################################
class Combination:
    def __init__(self, maxn:int=10**9, mod:int=1000000007) -> None:
        self.mod = mod
        self.maxn = maxn
        fac, facinv = [1]*(maxn+1), [1]*(maxn+1)
        for i in range(2, maxn + 1):
            fac[i] = fac[i-1] * i % mod
        facinv[-1] = pow(fac[-1], mod-2, mod)
        for i in range(maxn, 0, -1):
            facinv[i-1] = facinv[i] * i % mod
        self.fac = fac; self.facinv = facinv

    def nCr(self, n, r):
        """nCr
        n個のものからr個選ぶ
        """
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return self.fac[n] * self.facinv[r] * self.facinv[n-r] % self.mod

cmb = Combination(1000,1000000007)

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cmb.sum(A)
