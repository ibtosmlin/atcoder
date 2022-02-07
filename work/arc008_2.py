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
n, m = map(int, input().split())
name = list(input())
kit = list(input())

name = Counter(name)
kit = Counter(kit)

ret = 0
for k, v in name.items():
    if not k in kit:
        end(-1)
    u = kit[k]
    ret = max(ret, (v + u - 1) // u)

print(ret)