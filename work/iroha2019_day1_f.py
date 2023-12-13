# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
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

N, K = map(int, input().split())
P = prime_factorize(N)
if N == 1 or sum(P.values()) < K:
    exit(print(-1))

ret = []
for p in sorted(P.keys()):
    v = P[p]
    use = min(K-1, v)
    ret += [p] * use
    K -= use
    N //= pow(p, use)
    if K == 1: break
ret.append(N)
print(*ret)
