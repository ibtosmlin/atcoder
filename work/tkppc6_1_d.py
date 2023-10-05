# https://atcoder.jp/contests/tkppc6-1/tasks/tkppc6_1_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

mod = 998244353

n = int(input())
a = list(map(int, input().split()))
suma = [0]
for ai in a:
    suma.append(suma[-1] + ai)
suma.sort()

ret = 0
for i, bi in enumerate(suma):
    ret += (2*i - n) * bi % mod
    ret %= mod

print(ret)