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
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'




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

def inv_numbers(a: list) -> int:
    bit = BinaryIndexedTree(max(a) + 2)
    ret = 0
    for i, ai in enumerate(a):
        ret += i - bit.sum(ai)  #aiの位置より右側の合計=見てきた総計i - 左側の合計 => 反転数
        ret += bit.sum(ai) - bit.sum(ai-1)
        bit.add(ai, 1)          #aiの位置にメモ
    return ret

###################################


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))




ca = Counter(a)
cb = Counter(b)

if ca!=cb:
    print('No')
else:
    ta = inv_numbers(a)
    tb = inv_numbers(b)
    if (ta-tb)%2==0:
        print('Yes')
    elif max(ca.values())>=2:
        print('Yes')
    else:
        print('No')
