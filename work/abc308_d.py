# https://atcoder.jp/contests/abc308/tasks/abc308_d
from itertools import *
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys; sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i, base='a'): return chr(ord(base) + i%26)    # i=0->'a', i=25->'z'
def alpind(a, base='a'): return ord(a)-ord(base)
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def printyes(ret:bool): print('Yes' if ret else 'No')
def end(r=-1): exit(print(r))
h, w = map(int, input().split())
G = [input() for _ in range(h)]
if G[0][0] != 's':
    end('No')

direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}

seen = [[-1] * w for _ in range(h)]
snk = 'snuke'

que = deque()
que.append((0,0))
seen[0][0] = 0

while que:
    u, v = que.popleft()
    for du, dv in direc:
        nu = u + du
        nv = v + dv
        nc = (seen[u][v]+1)%5
        if notisinhw(nu, nv, h, w): continue
        if seen[nu][nv] != -1: continue
        if G[nu][nv] != snk[nc]: continue
        if nu == h-1 and nv == w-1:
            end('Yes')
        que.append((nu, nv))
        seen[nu][nv] = nc

end('No')

