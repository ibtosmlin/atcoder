# https://atcoder.jp/contests/abc331/tasks/abc331_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from collections import defaultdict

n, m, l = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ngs = defaultdict(int)
for _ in range(l):
    a, b = map(int1, input().split())
    ngs[A[a]+B[b]] += 1
A.sort(reverse=True)
B.sort(reverse=True)

ret = -1
for ai in A:
    if ai + B[0] < ret: break
    for bi in B:
        nm = ai + bi
        if ngs[nm] == 0:
            ret = max(ret, nm)
            break
        else:
            ngs[nm] -= 1
print(ret)
