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
n, x = map(int, input().split())
h = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(n-1):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

ret = 0
def dfs(cur, prev=-1):
    global ret
    if prev != -1 and len(edges[cur]) == 1:
        return h[cur]
    nw = h[cur]
    for nxt in edges[cur]:
        if nxt == prev: continue
        fg = dfs(nxt, cur)
        if fg: ret += 2
        nw |= fg
    return nw

dfs(x-1)
print(ret)