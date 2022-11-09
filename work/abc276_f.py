# https://atcoder.jp/contests/abc276/tasks/abc276_f
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
from bisect import bisect_right, insort_right

# 部分和の計算と要素の更新の両方を効率的に行える
# 1-indexed
# sum(r)        :閉区間 [0,r] の合計を取得する
# [8] a0 + a1  + a2 + a3 + a4 + a5 + a6 + a7
# [4] a0 + a1  + a2 + a3
# [2] a0 + a1               [6] a4 + a5
# [1] a0       [3] a2       [5] a4        [7] a6

#                   [1000]
#           [0100]
#   [0010]                [0110]
# [0001]    [0011]      [0111]      [1111]
class BinaryIndexedTree:
    # 初期化処理
    def __init__(self, size):
        self.size = size
        self.dat = [0]*(size+1)
        self.depth = size.bit_length()

    def init(self, a):
        for i, x in enumerate(a):
            self.add(i, x)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.dat[i] += x
            i += i & -i # 更新すべき位置

    def sum(self, r):
        """
        Returns
        -------
        sum of [0, r]
        """
        r += 1
        ret = 0
        while r>0:
            ret += self.dat[r]
            r -= r & -r # 加算すべき位置
        return ret

    def range_sum(self, l, r):
        """閉区間 [l,r] の合計を取得する

        Returns
        -------
        sum of [l, r]
        """
        if l == 0:
            return self.sum(r)
        else:
            return self.sum(r) - self.sum(l-1)


    def __getitem__(self, i):
        return self.range_sum(i, i)


    def right_bound_of_x(self, x):
        # pos       : sum([0, pos]) < x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] <= x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def right_bound_include_x(self, x):
        # pos       : sum([0, pos]) <= x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] < x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def left_bound_of_x(self, x):
        # pos   : x < sum([0, pos])  となる最小のindex
        return self.right_bound_include_x(x) - 1

    def left_bound_include_x(self, x):
        # pos   : x <= sum([0, pos])  となる最小のindex
        return self.right_bound_of_x(x) - 1


#### for debug
    def _get_original_sequence(self):
        ret = [self[i] for i in range(self.size)]
        return ret

    def _get_aggrigate_sequence(self):
        return [self.sum(i) for i in range(self.size)]

    def __str__(self):
        seq = self._get_original_sequence()
        ret = 'original :' + ' '.join(map(str, seq))
        ret += '\n'
        seq = self._get_aggrigate_sequence()
        ret += 'aggrigate:' + ' '.join(map(str, seq))
        return ret

########################################

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

bitcount = BinaryIndexedTree(200010)
bitvalue = BinaryIndexedTree(200010)

for i, ai in enumerate(a):
    ret = 0
    ret += 2 * bitcount.sum(ai) * ai
    ret += ai
    ret += 2 * bitvalue.range_sum(ai+1, 200000)
    ret %= mod1
    dp[i] = ret
    bitcount.add(ai, 1)
    bitvalue.add(ai, ai)

nw = 0
for i, dpi in enumerate(dp):
    k = i + 1
    nw += dpi
    nw %= mod1
    ninv = modinv(k, mod1)
    print(nw*ninv*ninv%mod1)
