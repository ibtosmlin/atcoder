# https://atcoder.jp/contests/past15-open/tasks/past202306_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
c, h = map(int, input().split())
if h >= 2800:
    print('o')
else:
    print('x')
