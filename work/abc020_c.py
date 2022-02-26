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
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
h, w, t = map(int, input().split())
g = [list(input()) for _ in range(h)]

for i, gi in enumerate(g):
    if not 'S' in gi: continue
    si = i
    sj = gi.index('S')

for i, gi in enumerate(g):
    if not 'G' in gi: continue
    gli = i
    glj = gi.index('G')


def is_ok(x):
    dp = [[10**10]*w for _ in range(h)]
    que = deque()
    que.append((si,sj))
    dp[si][sj] = 0
    while que:
        ci, cj = que.popleft()
        d = dp[ci][cj]
        for di, dj in [(1, 0), (-1, 0), (0,1), (0,-1)]:
            ni, nj = ci+di, cj+dj
            if ni<0 or ni>=h: continue
            if nj<0 or nj>=w: continue
            if g[ni][nj] == '#':
                nd = d+x
            else:
                nd = d+1
            if nd>=dp[ni][nj]: continue
            dp[ni][nj] = nd
            if not (gli==ni and glj==nj):
                que.append((ni, nj))

    return dp[gli][glj] <= t

ok = 1
ng = 10**10
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid): ok = mid
    else: ng = mid
print(ok)
