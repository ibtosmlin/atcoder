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
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)


dp = [-1] * n
cnt = 1

def dfs(cur, prev=-1):
    global dp, cnt
    if dp[cur] != -1:
        return dp[cur]

    if prev!=-1 and len(edges[cur])==1:
        dp[cur] = [cnt, cnt]
        cnt += 1
    else:
        mi = 10**6
        mn = -1
        for nxt in edges[cur]:
            if nxt==prev: continue
            minx, mnnx = dfs(nxt, cur)
            mi = min(mi, minx)
            mn = max(mn, mnnx)
        dp[cur] = [mi, mn]
    return dp[cur]

dfs(0)

for dpi in dp:
    print(*dpi)