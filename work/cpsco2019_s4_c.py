# https://atcoder.jp/contests/cpsco2019-s4/tasks/cpsco2019_s4_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from bisect import bisect_right
n, d = map(int, input().split())
R = list(map(int, input().split())) + [10**10]
R.sort()
# print(R)
ret = 0
for l, x in enumerate(R):
    r = bisect_right(R, x+d)
    m = max(r-l-1, 0)
    # print(l, r, m, m * (m-1) // 2)
    ret += m * (m-1) // 2
print(ret)