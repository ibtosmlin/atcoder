# https://atcoder.jp/contests/abc297/tasks/abc297_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

mod = 998244353
lim = 10**6
fac, facinv = [1]*(lim+1), [1]*(lim+1)
for i in range(2, lim + 1):
    fac[i] = fac[i-1] * i % mod
facinv[-1] = pow(fac[-1], mod-2, mod)
for i in range(lim, 0, -1):
    facinv[i-1] = facinv[i] * i % mod

def nCr(n, r):
    """nCr
    n個のものからr個選ぶ
    """
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return fac[n] * facinv[r] * facinv[n-r] % mod


H, W, K = map(int, input().split())

P = nCr(H*W, K)
P = pow(P, mod-2, mod)

def f(h, w):
    # 全部
    ret = nCr(h*w, K)
    # 1箇所
    ret -= nCr(max(0,h-1) * w, K) * 2
    ret -= nCr(h * max(0,w-1), K) * 2
    # 2
    ret += nCr(max(0,h-2) * w, K)
    ret += nCr(h * max(0,w-2), K)
    ret += nCr(max(0, h-1) * max(0,w-1), K) * 4
    # 3
    ret -= nCr(max(0, h-1) * max(0,w-2), K) * 2
    ret -= nCr(max(0, h-2) * max(0,w-1), K) * 2
    # 4
    ret += nCr(max(0, h-2) * max(0,w-2), K)
    return ret % mod

ret = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        ret += f(h, w) * (H-h+1) * (W-w+1) * h * w
        ret %= mod

print(ret*P%mod)