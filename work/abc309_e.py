# https://atcoder.jp/contests/abc309/tasks/abc309_e
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
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): exit(print(r))
n, m = map(int, input().split())
p = list(map(int, input().split()))

G = [[] for _ in range(n)]
for i in range(n-1):
    j = i + 1
    G[p[i]-1].append(j)

ins = [-1 for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    ins[x] = max(ins[x], y)

que = deque([0])
seen = [False] * n
seen[0] = True
while que:
    x = que.popleft()
    for nx in G[x]:
        if seen[nx]: continue
        if ins[x] > 0:
            ins[nx] = max(ins[nx], ins[x]-1)
        seen[nx] = True
        que.append(nx)



ret = 0
for i in ins:
    if i >= 0:
        ret += 1
print(ret)
