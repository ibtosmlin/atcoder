# https://atcoder.jp/contests/past16-open/tasks/past202309_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
m = int(input())
ret = 4<= m <= 9
print('Yes' if ret else 'No')
