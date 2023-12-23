# https://atcoder.jp/contests/abc332/tasks/abc332_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
k, g, m = map(int, input().split())
ng, nm = 0, 0

for _ in range(k):
    if ng == g:
        ng = 0
    elif nm == 0:
        nm = m
    else:
        t = min(g-ng, nm)
        ng += t
        nm -= t

print(ng, nm)