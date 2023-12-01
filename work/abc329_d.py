# https://atcoder.jp/contests/abc329/tasks/abc329_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
a = list(map(int, input().split()))

from heapq import heapify, heappop, heappush
que = []
C = [0] * (n+1)
for ai in a:
    C[ai] += 1
    heappush(que, (-C[ai], ai))
    print(que[0][1])
