from collections import defaultdict
from itertools import accumulate

n = int(input())
a = []
pm = dict()
for i in range(n):
    nw = defaultdict(int)
    q = int(input())
    for _ in range(q):
        p, e = map(int, input().split())
        nw[p] = e
        if not p in pm:
            pm[p] = [e, 1]
        else:
            ep, ec = pm[p]
            if ep > e:
                continue
            elif ep == e:
                pm[p] = [e, ec+1]
            else:
                pm[p] = [e, 1]
    a.append(nw)

ret = 0
for i in range(n):
    for p, e in a[i].items():
        if pm[p] == [e, 1]:
            ret += 1
            break

if ret < n:
    ret += 1
print(ret)
