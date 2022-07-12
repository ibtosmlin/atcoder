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
A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[-1] * (B+1) for _ in range(A+1)]
dp[A][B] = 0
for u in range(A)[::-1]:
    if (u+B)% 2== 0:
        dp[u][B] = dp[u+1][B] + a[u]
    else:
        dp[u][B] = dp[u+1][B]
for v in range(B)[::-1]:
    if (v+A)% 2== 0:
        dp[A][v] = dp[A][v+1] + b[v]
    else:
        dp[A][v] = dp[A][v+1]

for u in range(A)[::-1]:
    for v in range(B)[::-1]:
        if (u+v)%2 == 0:
            dp[u][v] = max(dp[u+1][v]+a[u], dp[u][v+1]+b[v])
        else:
            dp[u][v] = min(dp[u+1][v], dp[u][v+1])

print(dp[0][0])
