# https://atcoder.jp/contests/abc264/tasks/abc264_d
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
s = list(input())
t = list('atcoder')
n = 7
i = 0
while i < n and s[i] == t[i]:
    i += 1
if i == n: end(0)

ret = defaultdict(int)
que = deque([])
que.append(s)
ret[''.join(s)] = 0

while que:
    x = que.popleft()
    for u in range(n-1):
        nx = x[:]
        nx[u], nx[u+1] = nx[u+1], nx[u]
        if ''.join(nx) in ret: continue
        ret[''.join(nx)] = ret[''.join(x)] + 1
        que.append(nx)

print(ret[''.join(t)])
