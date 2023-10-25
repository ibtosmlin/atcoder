# https://atcoder.jp/contests/abc324/tasks/abc324_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
while n%2==0:
    n //=2
while n%3==0:
    n //=3
ret = n == 1
print('Yes' if ret else 'No')
