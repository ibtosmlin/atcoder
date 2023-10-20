# https://atcoder.jp/contests/past201912-open/tasks/past201912_n
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from heapq import heapify, heappop, heappush

n, c, d = map(int, input().split())

DA = [list(map(int, input().split())) for _ in range(n)]
if DA[0][0] != 1:
    DA = [[1, 0]] + DA

hq = []

ret = 0
for di, ai in DA[::-1]:
    c -= d - di
    d = di
    if c < 0:
        while hq and c < 0:
            x = - heappop(hq)
            c += x
            ret += 1
        if c < 0: exit(print(-1))
    heappush(hq, -ai)

print(ret)
