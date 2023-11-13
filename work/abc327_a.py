# https://atcoder.jp/contests/abc327/tasks/abc327_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000)
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
n = int(input())
S = input()
if 'ab' in S or 'ba' in S:
    print('Yes')
else:
    print('No')