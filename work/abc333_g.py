# https://atcoder.jp/contests/abc333/tasks/abc333_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from fractions import Fraction
r = Fraction(input())
N = int(input())
ret = (r - Fraction("1e-100")).limit_denominator(N)
print(ret.numerator, ret.denominator)