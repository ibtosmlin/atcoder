from bisect import bisect_right
from itertools import combinations

n, k, l, r = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
F = A[:n//2]
S = A[n//2:]

FL = []
for ki in range(k+1):
    ret = []
    for u in combinations(F, ki):
        ret.append(sum(u))
    ret.sort()
    FL.append(ret)

SL = []
for ki in range(k+1):
    ret = []
    for u in combinations(S, ki):
        ret.append(sum(u))
    ret.sort()
    SL.append(ret)

def f(x):
    ret = 0
    for ki in range(k+1):
        for u in FL[ki]:
            ret += bisect_right(SL[k-ki], x-u)
    return ret

print(f(r)-f(l-1))
