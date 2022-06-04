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
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()
n, p = map(int, input().split())
point = [0] * 3010
for i in range(3010):
    point[i] = i - len(str(i)) - 1

# dp[i][j]:Sはi文字使用して,変換後Tはj文字となっている文字列の数
dp = [[0] * 3010 for _ in range(3010)]
dps = [[0] * 3010 for _ in range(3010)]

dp[0][0] = 1
for i in range(n):
    dps[0][1] = dp[0][0]

for _ in range(n):
    if _ == 0:
        use = 26
    else:
        use = 25
    for i in range(3010):
        for j in range(3010):
            for k in range(3010-i):
                if j+point[k] >= 3010: continue
                dp[i+k][j+point[k]] += dp[i][j] * use
                dp[i+k][j+point[k]] %= p

print(dp[n])
