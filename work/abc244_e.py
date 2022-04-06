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

n, m, k, s, t, x = map(int, input().split())
s -= 1; t -= 1; x -= 1
edges = [[] for _ in range(n)]
for _ in range(m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

dp_o = [[0] * n for _ in range(k+1)]
dp_e = [[0] * n for _ in range(k+1)]
dp_e[0][s] = 1

for i in range(k):
    for fm in range(n):
        for to in edges[fm]:
            if to == x:
                dp_e[i+1][to] += dp_o[i][fm]
                dp_o[i+1][to] += dp_e[i][fm]
            else:
                dp_e[i+1][to] += dp_e[i][fm]
                dp_o[i+1][to] += dp_o[i][fm]
            dp_e[i+1][to] %= mod1
            dp_o[i+1][to] %= mod1

print(dp_e[k][t])
