# https://atcoder.jp/contests/past16-open/tasks/past202309_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)

n = int(input())
a = list(map(int, input().split()))

M = max(a)
R = 1000000000
unit = 10

ret = []
for ai in a:
    u = ai * R * unit // M
    u, r = divmod(u, unit)
    if r >= 5:
        u += 1
    ret.append(u)
print(*ret)