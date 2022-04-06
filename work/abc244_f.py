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
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

que = deque([])

dp = [[INF] * n  for _ in range(1<<n)]
for u in range(n):
    dp[0][u] = 0
    dp[1<<u][u] = 1
    que.append((1<<u, u))

while que:
    s, u = que.popleft()
    for v in edges[u]:
        if dp[s^(1<<v)][v] != INF: continue
        dp[s^(1<<v)][v] = dp[s][u] + 1
        que.append((s^(1<<v), v))

ret = 0
for i in range(1<<n):
    x = min(dp[i])
    ret += x
print(ret)
