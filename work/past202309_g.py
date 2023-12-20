# https://atcoder.jp/contests/past16-open/tasks/past202309_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from itertools import *
n = int(input())
A = list(map(int, input().split()))

tri = []
for i, j, k in combinations(range(n*3), 3):
    a, b, c = A[i], A[j], A[k]
    if a+b <= c: continue
    if b+c <= a: continue
    if c+a <= b: continue
    tri.append({i, j, k})


ret = 0
for p in combinations(tri, n-1):
    u = set(range(3*n))
    for pi in p:
        u -= set(pi)
    if len(u) != 3: continue
    if u in tri:
        ret += 1
print(ret//n)