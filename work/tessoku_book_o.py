# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_o
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
n = int(input())
a = list(map(int, input().split()))
class Compress:
    """一次元座標圧縮

    Parameters
    ----------
    points : list
         値のリスト [100,300,50,900,200]

    Returns
    -------
    pos : {50: 0, 100: 1, 200: 2, 300: 3, 900: 4}
    vals : {0: 50, 1: 100, 2: 200, 3: 300, 4: 900}
    list : [1, 3, 0, 4, 2]
    """
    def __init__(self, points, spacing=False, reverse=False):
        pos, vals, sx = {}, {}, set(points)
        if spacing: #スペースを作る場合
            for p in points: sx.add(p+1)

        for i, xi in enumerate(sorted(set(sx), reverse=reverse)):
            pos[xi], vals[i] = i, xi
        self.pos, self.vals = pos, vals
        self.original_list, self.list = points, [pos[xi] for xi in points]

    def __contains__(self, original_value):
        return original_value in self.pos.keys()


    def index(self, original_value):
        # 元value -> 新index
        if original_value in self: return self.pos[original_value]
        return None


    def value(self, index):
        # 新index -> 元value
        if index in self.vals: return self.vals(index)
        return None

x = Compress(a)
print(*[i+1 for i in x.list])