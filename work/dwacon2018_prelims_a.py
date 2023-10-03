# https://atcoder.jp/contests/dwacon2018-prelims/tasks/dwacon2018_prelims_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

s = input()
ret = s[0] == s[2] and s[1] == s[3]
print('Yes' if ret else 'No')