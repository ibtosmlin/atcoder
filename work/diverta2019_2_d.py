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
def dpr(n, A, B):
    dp = [0] * (n+1)
    dp[0] = 0
    for a, b in zip(A, B):
        v = b - a
        if v <= 0: continue
        for i in range(n-a+1):
            dp[i+a] = max(dp[i+a], dp[i] + v)
    n += max(dp)
    return n

n = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
n = dpr(n, A, B)
n = dpr(n, B, A)
print(n)
