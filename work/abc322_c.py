# https://atcoder.jp/contests/abc322/tasks/abc322_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
A = list(map(int, input().split()))

ret = [-1] * (n+1)

for ai in A:
    ret[ai] = 0

for i in range(n)[::-1]:
    if ret[i] == -1:
        ret[i] = ret[i+1] + 1

print('\n'.join(map(str, ret[1:])))