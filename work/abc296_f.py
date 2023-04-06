# https://atcoder.jp/contests/abc296/tasks/abc296_f
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()
# 転倒数
# 配列中 i<j, ai>ajとなるものの個数
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
# ex: a = [3, 5, 2, 0, 4, 1]  -> 10
# index: 0  1  2  3  4  5
# a    : 3  5  2  0  4  1
# bit_0:          1*        (a_0=3) 右側/反転数0
# bit_1:          1     1*  (a_1=5) 右側/反転数0
# bit_2:       1* 1     1   (a_2=2) 右側/反転数2
# bit_3: 1*    1  1     1   (a_3=0) 右側/反転数3
# bit_4: 1     1  1  1* 1   (a_4=4) 右側/反転数1
# bit_5: 1  1* 1  1  1  1   (a_5=1) 右側/反転数4

class BinaryIndexedTree:
    # 初期化処理
    def __init__(self, size):
        self.size = size
        self.dat = [0]*(size+1)
        self.depth = size.bit_length()

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.dat[i] += x
            i += i & -i # 更新すべき位置

    def sum(self, r):
        r += 1
        ret = 0
        while r>0:
            ret += self.dat[r]
            r -= r & -r # 加算すべき位置
        return ret

def compress(points:list) -> list:
    pos = {}
    sx = set(points)
    for i, xi in enumerate(sorted(set(sx))):
        pos[xi] = i
    return [pos[xi] for xi in points]

def inv_numbers(a: list) -> int:
    _a = compress(a)
    bit = BinaryIndexedTree(max(_a) + 2)
    ret = 0
    for i, ai in enumerate(_a):
        ret += i - bit.sum(ai)  #aiの位置より右側の合計=見てきた総計i - 左側の合計 => 反転数
        bit.add(ai, 1)          #aiの位置にメモ
    return ret

###################################

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if sorted(a) != sorted(b):
    end('No')
if list(Counter(a).most_common())[0][1] > 1:
    end('Yes')
print('Yes' if inv_numbers(a)%2 == inv_numbers(b)%2 else 'No')
