# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
a.sort()
mx = 0
mn = sum(a)
for i in range(n//2):
    x = a[i]+a[-i-1]
    mx = max(x, mx)
    mn = min(x, mn)
print(mx-mn)