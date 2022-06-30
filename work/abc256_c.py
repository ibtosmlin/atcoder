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
h1, h2, h3, w1, w2, w3 = map(int, input().split())
ret = 0
for x1 in range(31):
    for x2 in range(31):
        for y1 in range(31):
            for y2 in range(31):
                x3 = h1 - x1 -x2
                y3 = h2 - y1 -y2
                z1 = w1 - x1 - y1
                z2 = w2 - x2 - y2
                z3 = h3 - z1 - z2
                z3_ = w3 - x3 - y3
                if x1 <= 0: continue
                if x2 <= 0: continue
                if x3 <= 0: continue
                if y1 <= 0: continue
                if y2 <= 0: continue
                if y3 <= 0: continue
                if z1 <= 0: continue
                if z2 <= 0: continue
                if z3 <= 0: continue
                if z3 != z3_: continue
                ret += 1

print(ret)