import sys
from itertools import *
from bisect import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
h, w, n = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
rocks = [tuple(map(int, input().split())) for _ in range(n)]
INF = 10**10

yatx = dict()
xaty = dict()


for x, y in rocks:
    if x in yatx:
        yatx[x].append(y)
    else:
        yatx[x] = [-INF, y, INF]
    if y in xaty:
        xaty[y].append(x)
    else:
        xaty[y] = [-INF, x, INF]

for s in yatx.values():
    s.sort()
for s in xaty.values():
    s.sort()

seen = set()
ret = defaultdict(int)
seen.add((sx, sy))
que = deque([(sx, sy)])
ret[(sx, sy)] = 0


while que:
    cx, cy = que.popleft()
    nowd = ret[(cx, cy)]

    nxts = []
    if cy in xaty:
        p = bisect_left(xaty[cy], cx)
        if xaty[cy][p-1] != -INF:
            nxts.append([xaty[cy][p-1] + 1 , cy])
        p = bisect_right(xaty[cy], cx)
        if xaty[cy][p] != INF:
            nxts.append([xaty[cy][p] - 1 , cy])

    if cx in yatx:
        p = bisect_left(yatx[cx], cy)
        if yatx[cx][p-1] != -INF:
            nxts.append([cx, yatx[cx][p-1] + 1])
        p = bisect_right(yatx[cx], cy)
        if yatx[cx][p] != INF:
            nxts.append([cx, yatx[cx][p] - 1])

    for nx, ny in nxts:
        if (nx, ny) in seen: continue
        seen.add((nx, ny))
        ret[(nx, ny)] = nowd + 1
        que.append((nx, ny))

if (gx, gy) in ret:
    print(ret[(gx, gy)])
else:
    print(-1)
