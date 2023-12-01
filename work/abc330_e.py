# https://atcoder.jp/contests/abc330/tasks/abc330_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from sortedcontainers import SortedSet
n, q = map(int, input().split())
A = list(map(int, input().split()))
m = n+2
C = [0] * m
for ai in A:
    if ai <= m:
        C[ai] += 1

ss = SortedSet()
for i in range(m):
    if C[i] == 0:
        ss.add(i)

for _ in range(q):
    i, x = map(int, input().split())
    i -= 1
    y = A[i]
    A[i] = x
    if y <= m:
        C[y] -= 1
        if C[y] == 0:
            ss.add(y)
            ss.
    if x <= m:
        C[x] += 1
        if C[x] == 1:
            ss.remove(x)
    print(ss[0])
