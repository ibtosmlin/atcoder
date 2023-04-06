# https://atcoder.jp/contests/abc262/tasks/abc262_e
import sys
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1

#####################################
# nCr % 10**9+7
#####################################
mod, lim = 998244353, 10**6                   # mod素数, 出力の制限
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

n, m, k = map(int, input().split())
inc = [0] * n
for _ in range(m):
    u, v = map(int1, input().split())
    inc[u] ^= 1; inc[v] ^= 1

one = sum(inc)

ret = 0
for i in range(k+1):
    if i%2 : continue
    j = k - i
    ret += nCr(one, i) * nCr(n-one, j)
    ret %= mod
print(ret)
