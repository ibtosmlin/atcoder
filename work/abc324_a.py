# https://atcoder.jp/contests/abc324/tasks/abc324_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] != a[0]:
        exit(print('No'))
print('Yes')