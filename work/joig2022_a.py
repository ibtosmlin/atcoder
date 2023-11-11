# https://atcoder.jp/contests/joig2022-open/tasks/joig2022_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(sum(a[1:n-1]))