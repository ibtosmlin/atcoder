# https://atcoder.jp/contests/abc152/tasks/abc152_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from math import gcd
def lcm(a, b):
    return a*b//gcd(a, b)

n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    b.append(lcm(b[-1], a[i]))

print(b)