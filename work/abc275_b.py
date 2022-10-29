# https://atcoder.jp/contests/abc275/tasks/abc275_b
mod = 1000000007; mod1 = 998244353
L = list(map(int, input().split()))
_abc = L[:3]
_def = L[3:]

def prod(l):
    r = 1
    for li in l:
        r *= li
        r %= mod1
    return r

print((prod(_abc)-prod(_def))%mod1)
