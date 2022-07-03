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
n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]

ret = 0
for i in range(n):
    for j in range(n):
        for u in range(-1, 2):
            for v in range(-1, 2):
                if u == 0 and v == 0: continue
                nw = 0
                for k in range(n):
                    mu = i + u * k
                    mv = j + v * k
                    mu %= n
                    mv %= n
                    nw *= 10
                    nw += a[mu][mv]
                ret = max(ret, nw)
print(ret)