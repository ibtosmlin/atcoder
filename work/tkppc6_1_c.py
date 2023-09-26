# https://atcoder.jp/contests/tkppc6-1/tasks/tkppc6_1_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
c = a[0]

for i, ai in enumerate(a):
    if ai == -1:
        a[i] = c
a.sort()
ret = a[n-1] == c
print('Yes' if ret else 'No')
