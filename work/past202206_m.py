#####################################
# nCr % 10**9+7
#####################################
n = int(input())
mod, lim = 998244353, n+2                   # mod素数, 出力の制限
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

prob = pow()

ret = 0
for i in range(1, n):
    # (0,0) -> (i-1, i)   C(2*i-1, i)
