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

n, x = map(int, input().split())
s = input()

ds = []
cnt = 0
for si in s[::-1]:
    if si == 'U':
        cnt += 1
    else:
        if cnt == 0:
            ds.append(si)
        else:
            cnt -= 1

ds += ['U'] * cnt



for si in ds[::-1]:
    if si == 'L':
        x = x*2
    elif si == 'R':
        x = x*2 + 1
    else:
        x //= 2

print(x)