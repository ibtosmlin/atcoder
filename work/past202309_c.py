# https://atcoder.jp/contests/past16-open/tasks/past202309_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
a = list(map(int1, input().split()))
c = [0] * 8
for ai in a:
    c[ai] += 1
print(min(c))