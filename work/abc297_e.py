from heapq import *

n, k = map(int, input().split())
a = list(map(int, input().split()))

ret = set()
que = [0]
heapify(que)
for _ in range(k):
    num = heappop(que)
    for ai in a:
        if ai + num not in ret:
            ret.add(ai+num)
            heappush(que, ai+num)

print(sorted(ret)[k-1])
