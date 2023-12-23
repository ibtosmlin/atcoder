# https://atcoder.jp/contests/abc334/tasks/abc334_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from bisect import bisect_left, bisect_right
n, q = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
RR = [0]
for ri in r:
    RR.append(RR[-1] + ri)

for _ in range(q):
    x = int(input())
    print(bisect_right(RR, x)-1)