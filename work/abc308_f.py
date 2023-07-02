# https://atcoder.jp/contests/abc308/tasks/abc308_f
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
P = list(map(int, input().split()))
P.sort()

L = list(map(int, input().split()))
D = list(map(int, input().split()))
LD = sorted(zip(L, D))

Q = []

ret = sum(P)
i = 0
for p in P:
    while i < m and LD[i][0] <= p:
        heappush(Q, -LD[i][1])
        i += 1
    if Q:
        ret += heappop(Q)

print(ret)