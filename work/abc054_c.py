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

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
   a, b = map(int1, input().split())
   edges[a].append(b)
   edges[b].append(a)


P = list(permutations(range(1, n)))   # 順列(nPr)

ret = 0
seen = [False] * n
seen[0] = True

def dfs(c, v):
    global ret
    if sum(v) == n:
        ret += 1
        return
    for nx in edges[c]:
        if v[nx]: continue
        v[nx] = True
        dfs(nx, v)
        v[nx] = False

dfs(0, seen)

print(ret)
