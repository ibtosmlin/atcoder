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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])

mod, lim = 10**9+7, 10**6                   # mod素数, 出力の制限
g1, g2 = [[1]*(lim+1) for _ in range(2)]    # ！と逆元tbl
for i in range(2, lim + 1):
    g1[i] = g1[i-1] * i % mod
g2[-1] = pow(g1[-1], mod-2, mod)
for i in range(lim, 0, -1):
    g2[i-1] = g2[i] * i % mod

def fac(n): return g1[n]
def invfac(n): return g2[n]
def nCr(n, r):
    """nCr
    n個のものからr個選ぶ
    """
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)


def dfs(x, p=-1):
    ret = 1
    cnt = 0
    for nx in G[x]:
        if nx == p: continue
        petc, cntc = dfs(nx, x)
        cnt += cntc
        ret *= petc * invfac(cntc)
        ret %= mod
    ret *= fac(cnt)
    ret %= mod
    return ret, cnt + 1

ret = 0
for i in range(n):
    u, v = dfs(i)
    ret += u

ret = ret * invfac(2) % mod
print(ret)
