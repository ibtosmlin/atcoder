# https://atcoder.jp/contests/past202112-open/tasks/past202112_l
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
# 最長増加部分列 dp[k]
# 今まで見た来たものの中で、単調増加(非減少)な部分列であって、
# 長さ k であるようなもののうち、その最後の要素の最小値
# 新しいアイテムuだったとき
# dp[k] < u となる一番右の列(k)を特定しその次のdp[k+1]を小さければ更新する
# rem: kに対して単調増加
from bisect import bisect, bisect_left

class LIS:
    """
    fg: 0:単調非減少, 1:単調増加
    """
    def __init__(self, x:list, fg=1):
        n = len(x)
        res = [0] * n
        dp = []
        for i, xi in enumerate(x):
            if fg == 0: # 非減少
                pos = bisect(dp, xi)
            elif fg == 1: # 単調増加
                pos = bisect_left(dp, xi)
            res[i] = pos + 1
            if len(dp) <= pos:
                dp.append(xi)
            else:
                dp[pos] = xi
        self.length = len(dp)
        restore = []
        nw = self.length
        for i in range(n)[::-1]:
            if nw == res[i]:
                restore.append(x[i])
                nw -= 1
        restore.reverse()
        self.restore = restore
        self.lis = dp
        self.res = res



####################################
n, p = map(int, input().split())
a = list(map(int, input().split()))[::-1]
a = [ai - i for i, ai in enumerate(a) if 0<=ai-i<=p-n+1]

print(n - LIS(a, 0).length)
#print(a)
