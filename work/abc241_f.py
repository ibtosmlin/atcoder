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

ylistatx = dict()
xlistaty = dict()


ylistatx[sx] = set([-INF, INF])
xlistaty[sy] = set([-INF, INF])


for x, y in rocks:
    if x not in ylistatx:
        ylistatx[x] = set([-INF, INF])
    ylistatx[x].add(y)
    if y not in xlistaty:
        xlistaty[y] = set([-INF, INF])
    xlistaty[y].add(x)

ylx = {x: sorted(list(ylistatx[x])) for x in ylistatx}
xly = {y: sorted(list(xlistaty[y])) for y in xlistaty}

def search(a, x):
    ok = len(a)-1
    ng = 0
    while ok - ng > 0:


seen = set()
ret = defaultdict(int)
que = deque([(sx, sy)])
seen.add((sx, sy))
ret[(sx, sy)] = 0

while que:
    cx, cy = que.popleft()
    nowd = ret[(cx, cy)]

    p = ylx[cx][bisect_right(ylx[cx], cy)]
    if p<cy and p!=-INF:
        if (cx, p+1) in seen: continue
        que.append((cx, p+1))
        seen.add((cx, p+1))
        ret[(cx, p+1)] = nowd + 1

    p = ylx[cx][bisect_left(ylx[cx], cy)]
    if cy<p and p!=INF:
        if (cx, p-1) in seen: continue
        que.append((cx, p-1))
        seen.add((cx, p-1))
        ret[(cx, p-1)] = nowd + 1

    p = xly[cy][bisect_right(xly[cy], cx)]
    print(xly[cy], p)
    if p<cx and p!=-INF:
        if (p+1, cy) in seen: continue
        que.append((p+1, cy))
        seen.add((p+1, cy))
        ret[(p+1, cy)] = nowd + 1

    p = xly[cy][bisect_left(xly[cy], cx)]
    if cx<p and p!=INF:
        if (p-1, cy) in seen: continue
        que.append((p-1, cy))
        seen.add((p-1, cy))
        ret[(p-1, cy)] = nowd + 1

if (gx, gy) in ret:
    print(ret[(gx, gy)])
else:
    print(-1)

print(ret)