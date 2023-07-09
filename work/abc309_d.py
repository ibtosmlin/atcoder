# https://atcoder.jp/contests/abc309/tasks/abc309_d
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

n1, n2, m = map(int, input().split())
G = [[] for _ in range(n1+n2)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)



def bfs(x):
    seen = [-1] * (n1+n2)
    que = deque([x])
    seen[x] = 0
    while que:
        y = que.popleft()
        for ny in G[y]:
            if seen[ny] != -1: continue
            seen[ny] = seen[y] + 1
            que.append(ny)
    return max(seen)

print(1+bfs(0) + bfs(n1+n2-1))
