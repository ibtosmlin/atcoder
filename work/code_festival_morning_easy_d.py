# https://atcoder.jp/contests/code-festival-2014-morning-easy/tasks/code_festival_morning_easy_d
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(n)]
a = [int(input()) for _ in range(m)]
lr.sort()
a.sort()
ret = 0
que = []
idx = 0
heapify(que)
for ai in a:
    while idx<n and lr[idx][0] <= ai:
        heappush(que, (lr[idx][1], lr))
        idx += 1
    while que and que[0][0] < ai:
        heappop(que)
    if que:
        ret += 1
        heappop(que)
print(ret)
