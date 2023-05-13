# https://atcoder.jp/contests/tenka1-2015-quala/tasks/tenka1_2015_qualA_d
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
#関節 https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
#橋 https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_B
# グラフの橋・関節をO(n)で検出
import sys
sys.setrecursionlimit(10001000)

class LowLink():
    def __init__(self,G):
        self.N = len(G)
        self.G = G
        self.low = [-1] * self.N
        self.ord = [-1] * self.N
        self.t = -1

    def _dfs(self,x = 0,time = 0,p = -1):
        self.t += 1
        self.ord[x] = self.low[x] = self.t
        time += 1
        isArticulation = False
        cnt = 0 # 子の数
        for nx in self.G[x]:
            if self.low[nx] < 0:
                cnt += 1
                self._dfs(nx,time,x)
                self.low[x] = min(self.low[x],self.low[nx])
                if p != -1 and self.ord[x] <= self.low[nx]: isArticulation = True
                if self.ord[x] < self.low[nx]:
                    self.bridge.append((min(x,nx), max(x,nx)))
            elif nx != p:
                self.low[x] = min(self.low[x],self.ord[nx])

        if p == -1 and cnt >= 2: isArticulation = True
        if isArticulation: self.articulation.append(x)

    def build(self):
        self.articulation = []
        self.bridge = []
        self._dfs()


n, m = map(int,input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
#    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

ll = LowLink(G)
ll.build()
bridge = ll.bridge
all = len(bridge)
cnt = 0
for u, v in bridge:
    if len(ll.G[u]) == 1 or len(ll.G[v]) == 1: continue
    cnt += 1

if bridge and all - 1 <= cnt:
    print(all-1)
else:
    print('IMPOSSIBLE')
print(bridge)
print(low)