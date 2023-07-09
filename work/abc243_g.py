# https://atcoder.jp/contests/abc243/tasks/abc243_g
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
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r

n = 10 ** 5
dp = [0] * (n+1)
dp[1] = 1
rdp = 1
for i in range(2, n+1):
    sqrti = sqrt(i)
    if sqrti * sqrti == i:
        rdp += dp[sqrti]
    dp[i] = rdp

def solv(x):
    if x <= n:
        return dp[x]
    ret = 0
    sqrtx = sqrt(x)
    sqrtxx = sqrt(sqrtx)
    for i in range(1, sqrtxx+1):
        ret += max(0, sqrtx - i*i + 1) * dp[i]
    return ret

t = int(input())
for _ in range(t):
    print(solv(int(input())))
