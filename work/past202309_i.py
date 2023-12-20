# https://atcoder.jp/contests/past16-open/tasks/past202309_i
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from bisect import bisect_right

from heapq import heapify, heappop, heappush
n, m, k = map(int, input().split())
A = []
for i, ai in enumerate(list(map(int, input().split()))):
    A.append([ai//k, ai%k, i, ai])
A.sort()
R = [0]
for i in range(n-1):
    d = -A[i][0] + A[i+1][0]
    R.append(d*i+d)
for i in range(n-1):
    R[i+1] += R[i]

u = bisect_right(R, m)
for i in range(u):
    use = A[u-1][0] - A[i][0]
    m -= use
    A[i][0] += use
    A[i][-1] += use * k

A.sort()

h, r = divmod(m, u)
for i in range(u):
    A[i][0] += h
    A[i][-1] += h * k
    if i+1 <= r:
        A[i][0] += k
        A[i][-1] += k

ret = [0] * n
for _, __, i, c in A:
    ret[i] = c
print(*ret)