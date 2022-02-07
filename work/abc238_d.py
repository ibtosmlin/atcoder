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




def check(a, s):
    if a>s:
        return 'No'
    kuri = 0
    for i in range(60):
        an = a >> i & 1
        sm = s >> i & 1
        if an == 1:
            if sm == 0 and kuri == 0:
                kuri = 1
                continue
            if sm == 0 and kuri == 1:
                return 'No'
            if sm == 1 and kuri == 1:
                kuri = 1
                continue
            if sm == 1 and kuri == 0:
                return 'No'
        else:
            if sm == 0 and kuri == 0:
                kuri = 0
                continue
            if sm == 0 and kuri == 1:
                kuri = 1
                continue
            if sm == 1 and kuri == 0:
                kuri = 0
                continue
            if sm == 1 and kuri == 1:
                kuri = 0
                continue

    return 'Yes'



t = int(input())
for _ in range(t):
    a, s = map(int, input().split())
    print(check(a, s))