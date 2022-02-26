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

a, b, w = map(int, input().split())
w *= 1000
ret = 'UNSATISFIABLE'
num = []
for i in range(1, 1010000):
    if a*i<= w <=b*i:
        num.append(i)
if len(num)>0:
    print(min(num), max(num))
else:
    print(ret)
