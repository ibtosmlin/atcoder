# https://atcoder.jp/contests/arc159/tasks/arc159_a
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()
def fstr(x): return f'{x:.10f}'

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


    # 負値閉路検索
    @property
    def is_neg_cycle(self) -> bool:
        for i in range(self.n):
            if self.wf[i][i] < 0:
                return True
        return False


    # 経路復元
    def path(self, s, g):
        ret = []
        if s == g or self.wf[s][g] == self.INF:
            return ret
        cur = s
        while cur!=g:
            for nxt in range(self.n):
                if nxt==cur or nxt==s: continue
                if self.d[cur][nxt] + self.wf[nxt][g] == self.wf[cur][g]:
                    ret.append((cur, nxt))
    #                ret.append((nxt, cur))
                    cur = nxt
                    break
        return ret

##############################

n, k = map(int,input().split()) #N:頂点数 m:辺の数
A = [list(map(int, input().split())) for _ in range(n)]

WF = warshall_floyd(n*2)

for i in range(n*2):
    for j in range(n*2):
        if i == j: continue
        if A[i%n][j%n] == 1:
            WF.add_edge(i, j, 1)

WF.build()

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    s-=1; t-=1
    ns = s%n
    nt = t%n+(abs(s-t) >= n)*n
    ret = WF.wf[ns][nt]
    print(-1 if ret == INF else ret)

