# https://atcoder.jp/contests/code-thanks-festival-2017/tasks/code_thanks_festival_2017_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
from math import gcd
g = gcd(n, m)
print(n, m, g)