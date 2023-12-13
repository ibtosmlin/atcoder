# https://atcoder.jp/contests/abc331/tasks/abc331_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from collections import defaultdict

n, m, l = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
u = int((l+1)**0.5) + 2
ret = 0
for ai in A:
    for bi in B[:u]:
        ret = max(ret, ai+bi)
for ai in A[:u]:
    for bi in B:
        ret = max(ret, ai+bi)
print(ret)
