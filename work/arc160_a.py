# https://atcoder.jp/contests/arc160/tasks/arc160_a
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

n, k = map(int, input().split())
A = list(map(int, input().split()))
ret = []
for r in range(n):
    for l in range(r+1):
        B = A[:]
        B[l:r+1] = B[l:r+1][::-1]
        ret.append(B)
ret.sort()
u = k
for i, ri in enumerate(ret[:k]):
    # if ri[:u] == A[:u]:
        # print(ri[:u], A[:u])
        print(i+1, ri)

