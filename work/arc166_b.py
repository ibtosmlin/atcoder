# https://atcoder.jp/contests/arc166/tasks/arc166_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
from math import gcd
from collections import defaultdict
def lcm(x, a): return x * a // gcd(x, a)

N, a, b, c = map(int, input().split())
A = list(map(int, input().split()))

INF = 10**20
dp = defaultdict(lambda: INF)
for i in range(N):
    d = -A[i]
    ndp = defaultdict(lambda: INF)
    ndp['a'] = min(dp['a'], d%a)
    ndp['b'] = min(dp['b'], d%b)
    ndp['c'] = min(dp['c'], d%c)
    ndp['ab'] = min(dp['ab'], d%lcm(a, b), dp['a'] + d%b, dp['b'] + d%a)
    ndp['bc'] = min(dp['bc'], d%lcm(b, c), dp['b'] + d%c, dp['c'] + d%b)
    ndp['ca'] = min(dp['ca'], d%lcm(c, a), dp['c'] + d%a, dp['a'] + d%c)
    ndp['abc'] = min(dp['abc'], d%lcm(lcm(a, b), c))
    ndp['abc'] = min(ndp['abc'], dp['a'] + d%lcm(b, c))
    ndp['abc'] = min(ndp['abc'], dp['b'] + d%lcm(c, a))
    ndp['abc'] = min(ndp['abc'], dp['c'] + d%lcm(a, b))
    ndp['abc'] = min(ndp['abc'], dp['ab'] + d%c)
    ndp['abc'] = min(ndp['abc'], dp['bc'] + d%a)
    ndp['abc'] = min(ndp['abc'], dp['ca'] + d%b)
    dp = ndp

print(dp["abc"])