# https://atcoder.jp/contests/abc334/tasks/abc334_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

b, g = map(int, input().split())
if b > g:
    print('Bat')
else:
    print('Glove')