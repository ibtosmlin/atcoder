# https://atcoder.jp/contests/dp/tasks/dp_m
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
mod = 1000000007
# 1+x+x^2+...+x^ai
# https://atcoder.jp/contests/practice2/tasks/practice2_f
# https://atcoder.jp/contests/atc001/tasks/fft_c
# Σa_i * x^i * Σb_j * x^j  = Σ(Σa_i*b_j) * x ^t  t = i + jとなる場合の
# Σa_i*b_j の列を求める

g = 3   #primitive root
ginv = pow(g, mod-2, mod)

W = [pow(g, (mod-1)>>i, mod) for i in range(24)]
Winv = [pow(ginv, (mod-1)>>i, mod) for i in range(24)]

def fft(k, f):
    for l in range(1, k+1)[::-1]:
        d = 1 << l - 1
        U = [1]
        for i in range(d):
            U.append(U[-1]*W[l]%mod)
        for i in range(1<<k - l):
            for j in range(d):
                s = i*2*d + j
                f[s], f[s+d] = (f[s] + f[s+d])%mod, U[j]*(f[s] - f[s+d])%mod

def ifft(k, f):
    for l in range(1,k+1):
        d = 1 << l - 1
        for i in range(1<<k - l):
            u = 1
            for j in range(i*2*d, (i*2+1)*d):
                f[j+d] *= u
                f[j],f[j+d] = (f[j]+f[j+d])%mod, (f[j]-f[j+d])%mod
                u = u * Winv[l] % mod

def convolve(a, b):
    la, lb = len(a), len(b)
    le = la + lb - 1
    k = le.bit_length()
    n = 1 << k
    ninv = pow(n,mod-2,mod)
    a += [0]*(n-la)
    b += [0]*(n-lb)
    fft(k,a)
    fft(k,b)
    a = [ai * bi % mod for ai, bi in zip(a, b)]
    ifft(k,a)
    return [ai * ninv % mod for ai in a[:le]]

n, k = map(int, input().split())
A = list(map(int, input().split()))

from sympy import fps
fps()