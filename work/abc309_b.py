# https://atcoder.jp/contests/abc309/tasks/abc309_b
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
n = int(input())
A = []
for _ in range(n):
    x = list(input())
    A.append(x)

B = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            B[i][j] = A[i+1][j]
        elif i == 0:
            B[i][j] = A[i][j-1]
        elif j == n-1:
            B[i][j] = A[i-1][j]
        elif i == n-1:
            B[i][j] = A[i][j+1]
        elif j == 0:
            B[i][j] = A[i+1][j]
        else:
            B[i][j] = A[i][j]
for bi in B:
    print(''.join(bi))

