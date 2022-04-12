import enum
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


class Imos:
    def __init__(self, a:list):
        self.origin = a
        self.accum = [0]
        for ai in a:
            self.accum.append(self.accum[-1] + ai)
        self.n = self.accum
        self.INF = float('inf')

    def _get_max(self, accum:list):
        """
        区間和(ar-al)の最大値
        max(ar-min(al))
        """
        ret_min = - self.INF
        min_al = self.INF
        for ar in accum:
            min_al = min(ar, min_al)
            ret_min= max(ar - min_al, ret_min)
        return ret_min

    @property
    def get_max(self):
        return self._get_max(self.accum)

    @property
    def get_min(self):
        return - self._get_max([-ai for ai in self.accum])


n = int(input())
a = list(map(int, input().split()))
for i, ai in enumerate(a):
    if ai==0:
        a[i] = -1

im = Imos(a)
print(im.get_max - im.get_min + 1)
