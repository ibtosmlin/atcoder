# https://atcoder.jp/contests/abc318/tasks/abc318_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
from collections import defaultdict
C = defaultdict(list)
for i, ai in enumerate(a):
    C[ai].append(i)

ret =0
for x in C.values():
    x.sort()
    m = len(x)
    for i in range(m-1):
        ret += (x[i+1] - x[i] -1) * (i+1) * (m-i-1)
print(ret)