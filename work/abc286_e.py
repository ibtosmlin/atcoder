# https://atcoder.jp/contests/abc286/tasks/abc286_e
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
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()
import copy

class warshall_floyd:
    def __init__(self, n:int) -> None:
        self.INF = 10**20
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
                    if wf[i][k] != self.INF and wf[k][j] != self.INF:
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


##############################

n = int(input())
a = list(map(int, input().split()))
s = [input() for _ in range(n)]
INF = 10**9
OFF = 10**13

WF = warshall_floyd(n)

for u in range(n):
    for v in range(n):
        if s[u][v] == 'N': continue
        w = INF - a[u] + OFF
        WF.add_edge(u, v, w)

WF.build()

q = int(input())
for _ in range(q):
    u, v = map(int1, input().split())
    ret = WF.wf[u][v]
    if ret == WF.INF:
        print('Impossible')
        continue
    x, y = divmod(ret, OFF)
    y = x * INF - y
    print(x, y + a[v])
