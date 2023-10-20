# https://atcoder.jp/contests/abc323/tasks/abc323_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import defaultdict
from heapq import heapify, heappop, heappush

n = int(input())
sc = dict()
hq = []
for _ in range(n):
    s, c = map(int, input().split())
    sc[s] = c
    heappush(hq, s)

cnt = 0
while hq:
    if hq[0] <= 10**9:
        s = heappop(hq)
        c = sc[s]
        cnt += c%2
        t = 2*s
        if c//2:
            if not t in sc:
                heappush(hq, t)
                sc[t] = 0
            sc[t] += c//2
    else:
        s = heappop(hq)
        c = sc[s]
        cnt += bin(c).count('1')

print(cnt)