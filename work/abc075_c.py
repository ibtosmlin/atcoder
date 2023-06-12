# https://atcoder.jp/contests/abc075/tasks/abc075_c
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

n, m = map(int, input().split())
G = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, i))
    G[b].append((a, i))


def dfs(x, i):
    global seen
    seen.add(x)
    for nx, j in G[x]:
        if nx in seen: continue
        if i == j: continue
        dfs(nx, i)


ret = 0
for i in range(m):
    seen = set()
    dfs(0,i)
    if len(seen) != n:
        ret += 1
print(ret)