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

import copy

class warshall_floyd:
    def __init__(self, n:int) -> None:
        self.INF = float("inf")
        self.n = n
        self.d = [[self.INF] * n for _ in range(n)]
        #d[u][v] : 辺uvのコスト(存在しないときはinf)
        for i in range(n):
            self.d[i][i] = 0 #自身のところに行くコストは０



    def build(self):
        n = self.n
        wf = copy.deepcopy(self.d)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])

        self.wf = wf #wf[i][j]に頂点i, j間の最短距離を格納


    def add_edge(self, fm, to, cost):
        self.d[fm][to] = cost

##############################

n, m, r =map(int, input().split())
R = list(map(int1, input().split()))

WF = warshall_floyd(n)

for _ in range(m):
    _u, _v, _w = map(int,input().split())
    _u -= 1; _v -= 1
    WF.add_edge(_u, _v, _w)
    WF.add_edge(_v, _u, _w)

WF.build()

P = list(permutations(range(r)))   # 順列(nPr)

ret = INF
for pi in P:
    nw = 0
    for i in range(r-1):
        nw += WF.wf[R[pi[i]]][R[pi[i+1]]]
    ret = min(ret, nw)
print(ret)