# https://atcoder.jp/contests/arc165/tasks/arc165_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

##############################
# 素因数分解
# nは10**15くらいまでOK
# returns dict s.t. key = {prime}   value = {degree}
##############################
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

def solve():
    n = int(input())
    q = prime_factorize(n)
    if len(q) >= 2:
        print('Yes')
    else:
        print('No')


t = int(input())
for _ in range(t):
    solve()