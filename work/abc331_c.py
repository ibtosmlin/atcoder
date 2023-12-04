# https://atcoder.jp/contests/abc331/tasks/abc331_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))
B = [0]
for ai in sorted(a):
    B.append(B[-1] + ai)

A = a[:]
A.sort()

for ai in a:
    u = bisect_right(A, ai)
    print(B[-1] - B[u])