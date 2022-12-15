# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ct
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
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
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
                if S[i] == T[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    def __len__(self):
        # LCSの長さ
        return self.dp[self.ls][self.lt]

    def __str__(self):
        # 復元
        ret = []
        i, j = self.ls, self.lt
        dp = self.dp
        while i and j:
            # (i-1, j) -> (i, j) と更新されていた場合
            if dp[i][j] == dp[i-1][j]:
                i-=1   # DP の遷移を遡る
            # (i, j-1) -> (i, j) と更新されていた場合
            elif dp[i][j] == dp[i][j-1]:
                j-=1   # DP の遷移を遡る
            # (i-1, j-1) -> (i, j) と更新されていた場合
            else:
                ret.append(self.S[i-1])
                # このとき s[i-1] == t[j-1] なので、t[j-1] + res でも OK
                i-=1
                j-=1   # DP の遷移を遡る
        ret = ret[::-1]
        if self.Type == str: ret = ''.join(ret)
        return ''.join(ret)


#####################
n = int(input())
s = list(input())
t = s[::-1]
lcs = LCS(s, t)
print(len(lcs))
