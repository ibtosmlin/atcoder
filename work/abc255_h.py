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

    def rangesum(self, l, r):
        """閉区間 [l,r] の合計を取得する

        Returns
        -------
        sum of [l, r]
        """
        if l == 0:
            return self.sum(r)
        else:
            return self.sum(r) - self.sum(l-1)


    def get(self, i):
        return self.rangesum(i, i)


    def lower_bound(self, x):
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] < x:
                sum_ += self.dat[k]
                pos += 1 << i
        # pos = sum(i) < xとなる最大のindex
        # pos + 1 = sum(i) >= xとなる最小のindex
        return pos  #0-indexed


#### for debug
    def _get_original_sequence(self):
        ret = [self.get(i) for i in range(self.size)]
        return ret

    def _get_aggrigate_sequence(self):
        return [self.sum(i) for i in range(self.size)]

    def __str__(self):
        seq = self.get_original_sequence()
        ret = 'original :' + ' '.join(map(str, seq))
        ret += '\n'
        seq = self.get_aggrigate_sequence()
        ret += 'aggrigate:' + ' '.join(map(str, seq))
        return ret


n, q = map(int, input().split())
D = []
L = []
R = []
pt = set()
pt.add(0)
pt.add(n)
pt.add(n+1)
for i in range(q):
    d, l, r = map(int, input().split())
    D.append(d)
    L.append(l)
    R.append(r)
    pt.add(d)
    pt.add(d+1)
    pt.add(l)
    pt.add(l-1)
    pt.add(r)
    pt.add(r-1)
pt = list(pt)
pt.sort()
dic = dict()
for i, pti in enumerate(pt):
    dic[pti] = i

print(pt)
print(dic)


########################################

bit = BinaryIndexedTree(len(pt))
bit.init([0]*len(pt))

pd = 0
for i in range(q):
    d = D[i]
    l = L[i]
    r = R[i]
    for j in range(dic[pd]+1, dic[d]+1):
        (pt[j] + pt[j-1] + 1) * (pt[j] - pt[j-1] + 1) // 2