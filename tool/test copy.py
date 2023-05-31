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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()

class Bit:
    def __init__(self, x=0, n=32): self.x = x; self.n = n
    def __bool__(self): return self.x != 0
    def __int__(self): return self.x
    def __str__(self): return f'{self.x}: {self.bin}'
    def __len__(self): return self.n

    @property
    def size(self): return 1 << self.n
    @property
    def bin(self): return ('0' * self.n + bin(self.x)[2:])[-self.n:]
    @property
    def all(self): return Bit(self.size-1, self.n)  #すべて1
    @property
    def other(self): return self ^self.all          #反転


    def __add__(self, other): return Bit(self.x + other.x, max(self.n, other.n))
    def __sub__(self, other): return Bit(self.x - other.x, max(self.n, other.n))

    def __and__(self, other): return Bit(self.x & other.x, max(self.n, other.n))
    def __or__(self, other): return Bit(self.x | other.x, max(self.n, other.n))
    def __xor__(self, other): return Bit(self.x ^ other.x, max(self.n, other.n))

    def __eq__(self, other): return self.x == other.x
    def __ne__(self, other): return self.x != other.x


    def mask(self, mask):
        if type(mask) == int: mask = Bit(mask, self.n)
        return self & mask

    def set(self, mask):
        if type(mask) == int: mask = Bit(mask, self.n)
        return self | mask

    def bit_mask(self, k:int):
        return self.mask(1<<k)

    def bit_set(self, k:int):
        return self.set(1<<k)

    def bit_set(self, k:int):
        return self.set(1<<k)


u = Bit(30, 10)
v = Bit(5, 10)
print(u)
print(v)
print(u&v)
print(u.mask(v))
print(u.set(v))
print(u.bit_set(8))
print(u.bit_mask(2))
