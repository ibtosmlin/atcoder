# https://atcoder.jp/contests/abc289/tasks/abc289_e
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

def solve():
    n, m = map(int, input().split())
    C = list(map(int, input().split()))
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        G[u].append(v)
        G[v].append(u)
    que = deque()
    seen = [[-1]*n for _ in range(n)]
    que.append((0, n-1))
    seen[0][n-1] = 0
    while que:
        x, y = que.popleft()
        nw = seen[x][y]
        for nx in G[x]:
            for ny in G[y]:
                if seen[nx][ny] != -1: continue
                if C[nx] == C[ny]: continue
                que.append((nx, ny))
                seen[nx][ny] = nw + 1
                if nx == n-1 and ny == 0:
                    return seen[nx][ny]
    return -1

t = int(input())
for _ in range(t):
    print(solve())
