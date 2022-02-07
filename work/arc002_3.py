import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'

n = int(input())
s = input()

t = "ABXY"

PN = list(product(t, repeat=2)) # 重複順列(n**r)


def cnt(l, r):
    l = "".join(l)
    r = "".join(r)
    dp = [10**10] * (n+1)
    dp[0] = 0
    for i in range(n):
        if i<n-1 and (s[i:i+2] == l or s[i:i+2] == r):
            dp[i+2] = min(dp[i] + 1, dp[i+2])
        else:
            dp[i+1] = min(dp[i] + 1, dp[i+1])
    return dp[n]


ret = n
for l in PN:
    for r in PN:
        if l==r: continue
        ret = min(ret, cnt(l, r))

print(ret)