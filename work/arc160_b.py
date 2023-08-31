# https://atcoder.jp/contests/arc160/tasks/arc160_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

mod = 998244353
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r

def f(n):
    ret = 0
    for y in range(1, sqrt(n)+1):
    # x < y < z:
        # x: 1<= x < y
        # z: y< z <= int(n/y)
        ret += 6 * (y-1) * (int(n//y)-y) % mod
        ret %= mod
    # x == y < z:
        # x: 1<= x = y
        # z: y< z <= int(n/y)
        ret += 3 * (int(n//y)-y) % mod
        ret %= mod
    # x < y == z:
        # x: 1<= x < y
        # z: y== z <= int(n/y)
        ret += 3 * (y-1) % mod
        ret %= mod
    # x == y == z:
        ret += 1
        ret %= mod
    return ret

t = int(input())
for _ in range(t):
    n = int(input())
    print(f(n))


