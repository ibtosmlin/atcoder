# https://atcoder.jp/contests/tenka1-2016-qualb/tasks/tenka1_2016_qualB_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

def f(n): return (n*n+4) // 8
print(f(f(f(20))))