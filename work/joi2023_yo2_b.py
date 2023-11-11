# https://atcoder.jp/contests/joi2023yo2/tasks/joi2023_yo2_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
from bisect import bisect_left

n = int(input())
X = []
for _ in range(4):
    a = sorted(map(int, input().split()))
    X.append(a)


def f(x):
    ret = 0
    for xi in X:
        u = bisect_left(xi, x)
        if u == n: return 10**10
        ret = max(xi[u], ret)
    return ret-x

ret = 10**10

for xi in X:
    for xij in xi:
        ret = min(f(xij), ret)

print(ret)