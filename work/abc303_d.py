# https://atcoder.jp/contests/abc303/tasks/abc303_d
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()
x, y, z = map(int, input().split())
s = input()
n = len(s)
dp = [[INF1] * 2 for _ in range(n+1)]
dp[0][0] = 0

for i, si in enumerate(s):
    if si == 'A':
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + y)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + z + x)
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + z + y)
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + x)
    else:
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + x)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + z + y)
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + z + x)
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + y)

print(min(dp[-1]))