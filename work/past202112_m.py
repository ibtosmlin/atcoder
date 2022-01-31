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

def compress(points, reverse=False, spacing=False):
    """一次元座標圧縮

    Parameters
    ----------
    points : list
         値のリスト [100,300,50,900,200]

    Returns
    -------
    pos : {50: 0, 100: 1, 200: 2, 300: 3, 900: 4}
    vals : {0: 50, 1: 100, 2: 200, 3: 300, 4: 900}
    """
    pos = {}
    vals = {}
    sx = set(points)
    if spacing:
        for p in points:
            sx.add(p+1)

    for i, xi in enumerate(sorted(set(sx), reverse=reverse)):
        pos[xi] = i
        vals[i] = xi
    sx_cmp = [pos[xi] for xi in sx]
    return pos, vals, sx_cmp


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

########################################


n, q = map(int, input().split())
s = list(input().split())
ts = set(s)
query = []
for _ in range(q):
    x, t = input().split()
    x = int1(x)
    query.append((x, t))
    ts.add(t)

pos, vals, _ = compress(ts)
n = len(pos)
bit = BinaryIndexedTree(n)
for si in s:
    bit.add(pos[si], 1)

for k, si in query:
    fmi = bit.lower_bound(k) + 1
    toi = pos[si]
    bit.add(fmi, -1)
    bit.add(toi, 1)

print(bit._get_original_sequence())

ret = []
for i in range(n):
    for j in range(bit.get(i)):
        ret.append(vals[j])
print(*ret)