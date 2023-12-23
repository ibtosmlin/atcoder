# https://atcoder.jp/contests/abc332/tasks/abc332_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n, m = map(int, input().split())
s = list(input().split('0'))


logo = 0
for si in s:
    logo = max(logo, si.count('2'))

ret = 0
for si in s:
    ret = max(ret, logo + max(0, len(si) - (logo+m)))
print(ret)