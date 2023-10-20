# https://atcoder.jp/contests/arc167/tasks/arc167_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

mod = 998244353
hf = pow(2, mod-2, mod)

def prime_factorize(n:int) -> dict:
    if n == 1: return {1: 1}
    pd = dict()
    for p in range(2, int(n**0.5)+1):
        if n % p != 0: continue
        d = 0
        while n % p == 0:
            d += 1
            n //= p
        pd[p] = d
    if n != 1: pd[n] = 1
    return pd

A, B = map(int, input().split())
L = B
is_even = B%2

for _, e in prime_factorize(A).items():
    L = L * (e * B + 1) % mod
    is_even = is_even * (e * B + 1) % 2

if is_even: L -= 1

print(L * hf % mod)
