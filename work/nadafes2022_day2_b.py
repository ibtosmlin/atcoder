# https://atcoder.jp/contests/nadafes2022_day2/tasks/nadafes2022_day2_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ret = max(a) * min(b)
for i in range(n):
    ret = min(ret, a[i]*b[i])
print(ret)