# https://atcoder.jp/contests/abc326/tasks/abc326_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

x, y  = map(int, input().split())
if -3 <=  y - x <= 2:
    ret = 'Yes'
else:
    ret = 'No'
print(ret)