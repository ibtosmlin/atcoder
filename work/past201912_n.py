# https://atcoder.jp/contests/past201912-open/tasks/past201912_n
import sys; sys.setrecursionlimit(10001000)
def input(): return sys.stdin.readline().rstrip()
from bisect import bisect_left

n, w, c = map(int, input().split())

def solv(rock):
    pos = {0, w, w+1}
    for l, r, _c in rock:
        pos.add(l)
        pos.add(r)
    m = len(pos)
    X = sorted(pos)
    dpos = {pi: i for i, pi in enumerate(X)}
    CX = [0] * (m+1)

    for l, r, cos in rock:
        CX[dpos[l]+1] += cos
    for i in range(m):
        CX[i+1] += CX[i]

    print(X)
    print(CX)

    ret = 10**15
    for lp in range(m):
        if X[lp] + c > w: break
        rp = bisect_left(X, X[lp]+c)
        if rp != m:
            print(lp, rp,X[lp],X[rp], CX[rp], CX[lp], CX[rp] - CX[lp])
            ret = min(ret, CX[rp] - CX[lp])
    return ret

rock = []
rockr = []
for _ in range(n):
    l, r, cos = map(int, input().split())
    rock.append((l, r, cos))
    rockr.append((w-r, w-l, cos))

ret = min(solv(rock), solv(rockr))
print(ret)





