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
c = list(map(int, input().split()))
x = list(map(int, input().split()))
d = defaultdict(list)
for ci, xi in zip(c, x):
    d[ci].append(xi)
ret = inv_numbers(x)
for dx in d.values():
    ret -= inv_numbers(dx)
print(ret)
