import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
n = int(input())
a, b = map(int, input().split())
a -= 1; b -= 1
m = int(input())
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

que = deque([])
que.append(a)
dp = [INF] * n
dp[a] = 0
ret = [0] * n
ret[a] = 1

while que:
    c = que.popleft()
    for nx in edges[c]:
        if dp[nx] == dp[c]+1:
            ret[nx] += ret[c]
        elif dp[nx] == INF:
            ret[nx] += ret[c]
            dp[nx] = dp[c]+1
            que.append(nx)
        ret[nx] %= mod
print(ret[b])
