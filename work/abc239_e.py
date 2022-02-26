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



n, q = map(int, input().split())
x = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(n-1):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

queries = []
for i in range(q):
    v , k = map(int, input().split())
    v -= 1
    queries.append((v, k))

subs = [[] for _ in range(n)]
fixed = [False] * n



def dfs(cur, prev=-1):
    if fixed[cur]:
        return subs[cur]
    elif len(edges[cur]) == 1 and prev!=-1:
        fixed[cur] = True
        subs[cur] = [x[cur]]
        return subs[cur]
    ret = [x[cur]]
    for nxt in edges[cur]:
        if nxt == prev: continue
        ret += dfs(nxt, cur)
    ret.sort(reverse=True)
    subs[cur] = ret[:20]
    fixed[cur] = True
    return subs[cur]


dfs(0)


for v, k in queries:
    print(subs[v][k-1])
