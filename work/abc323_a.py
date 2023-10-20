# https://atcoder.jp/contests/abc323/tasks/abc323_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

s = input()
if '1' in s[1::2]:
    print('No')
else:
    print('Yes')
    