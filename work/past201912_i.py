import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
n, m = map(int, input().split())

dp = [INF] * (1<<n)
dp[0] = 0
for i in range(m):
    s, c = input().split()
    s=s.replace('Y', '1').replace('N', '0')
    s=int(s, 2)
    for j in range(1<<n):
        dp[j|s] = min(dp[j] + int(c), dp[j|s])

ret = dp[-1]
print(-1 if ret == INF else ret)
