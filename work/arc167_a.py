# https://atcoder.jp/contests/arc167/tasks/arc167_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = A[n-m:]
for i, ai in enumerate(A[:n-m][::-1]):
    B[i] += ai
ret = 0
for bi in B:
    ret += bi ** 2
print(ret)