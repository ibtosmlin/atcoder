# https://atcoder.jp/contests/abc308/tasks/abc308_e
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
n = int(input())
A = list(map(int, input().split()))
S = input()

from functools import lru_cache
@lru_cache()
def mex(i, j, k):
    u = [True] * 4
    u[i] = u[j] = u[k] = False
    for x in range(4):
        if u[x]: return x


RM = [[0] * 3 for _ in range(n+1)]
RX = [[0] * 3 for _ in range(n+1)]

for i in range(n):
    if S[i] == 'M':
        RM[i+1][A[i]] += 1
    if S[i] == 'X':
        RX[i+1][A[i]] += 1

for i in range(n):
    for j in range(3):
        RM[i+1][j] += RM[i][j]
        RX[i+1][j] += RX[i][j]

ret = 0
for t in range(n):
    if S[t] != 'E': continue
    for i in range(3):
        for j in range(3):
            ret += RM[t][i] * (RX[-1][j] - RX[t][j]) * mex(i, j, A[t])
            # ret += RM[t][i] * (RX[-1][j] - RX[t][j]) * mex([i, j, A[t]])

print(ret)

