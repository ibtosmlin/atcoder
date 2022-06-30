import sys
from itertools import *
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
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()


################

n = int(input())
p = []
for i in range(n):
    x, y, pi = map(int, input().split())
    p.append((x, y, pi))

edges = [[] for _ in range(n)]
for i in range(n):
    xi, yi, pi = p[i]
    for j in range(n):
        xj, yj, _ = p[j]
        if i == j: continue
        edges[i].append((j, pi, abs(xi-xj)+abs(yi-yj)))

def bfs(s):
    for x in range(n):
        seen = [False] * n
        q = deque([x])
        seen[x] = True
        while q:
            cur = q.popleft()
            for nx, px, dx in edges[cur]:
                if seen[nx]: continue
                if s * px < dx: continue
                q.append(nx)
                seen[nx] = True
        if sum(seen)==n:
            return True
    return False

ok = 10**10
ng = 0

while ok-ng > 1:
    mid = (ok+ng)//2
    if bfs(mid):
        ok = mid
    else:
        ng = mid
print(ok)