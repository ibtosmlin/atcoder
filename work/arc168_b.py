# https://atcoder.jp/contests/arc168/tasks/arc168_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
a = list(map(int, input().split()))

xor = 0
for ai in a:
    xor ^= ai
if xor: exit(print(-1))

from collections import Counter
A = Counter(a)
m = -1
for k, v in A.items():
    if v % 2: m = max(m, k)
if m == -1:  exit(print(0))
print(m-1)