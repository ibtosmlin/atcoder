# https://atcoder.jp/contests/past16-open/tasks/past202309_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
a, b, c = map(int, input().split())
ret = a == b == c
print('Yes' if ret else 'No')
