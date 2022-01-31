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

#####################################
# LCS(longest common sequence)
# 部分列で最長の共通のもの
#####################################
# https://atcoder.jp/contests/dp/tasks/dp_f

# dp[i+1][j+1]:= s の i 文字目までと t の j 文字目まででの LCS の長さ
class LCS:
    def __init__(self, S, T) -> None:
        self.Type = type(S)
        if self.Type == str:
            S = list(S)
            T = list(T)
        self.S = S
        self.T = T
        self.ls = len(S)
        self.lt = len(T)
        self.dp = [[0]*(self.lt+1) for _ in range(self.ls+1)]
        dp = self.dp
        for i in range(self.ls):
            for j in range(self.lt):
                if S[i] % T[j] == 0:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])


    def length(self):
        # LCSの長さ
        return self.dp[self.ls][self.lt]



#####################
n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
lcs = LCS(s, t)
print(lcs.length())