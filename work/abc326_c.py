# https://atcoder.jp/contests/abc326/tasks/abc326_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from bisect import bisect_left
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ret = 0
for i in range(n):
    now = bisect_left(a, a[i]+m) - i
    ret = max(ret, now)
print(ret)