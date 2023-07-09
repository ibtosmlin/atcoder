# https://atcoder.jp/contests/abc230/tasks/abc230_f
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
a = list(map(int, input().split()))
dp = {0: 1}

for i, ai in enumerate(a):
    ndp = defaultdict(int)
    t = 0
    for k, v in dp.items():
        t = t + v % mod1
        ndp[k+ai] += v
        ndp[k+ai] %= mod1
    if i:
        ndp[ai] += t
        ndp[ai] % mod1
    dp = ndp

ret = 0
for v in dp.values():
    ret +=v
print(ret)