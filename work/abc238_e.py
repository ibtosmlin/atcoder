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
n, q = map(int, input().split())


que = []
for _ in range(q):
    l, r = map(int1, input().split())
    que.append((l, r+1))
edges = [[] for _ in range(n+1)]
for _a, _b in que:
    edges[_a].append(_b)
    edges[_b].append(_a)


dp = [-1] * (n+1)
que = deque()
que.append(0)
dp[0] = 1
while que:
    cur = que.popleft()
    for nxt in edges[cur]:
        if dp[nxt]!=-1: continue
        dp[nxt] = 1
        que.append(nxt)

if dp[n] == 1:
    print('Yes')
else:
    print('No')