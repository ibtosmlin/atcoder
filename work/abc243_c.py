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

dic_rmin = dict([])
dic_lmax = dict([])

n = int(input())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append([x, y])

s = input()

for (x, y), si in zip(pos, s):
    if si == 'R':
        if not y in dic_rmin:
            dic_rmin[y] = x
        else:
            dic_rmin[y] = min(dic_rmin[y], x)
    else:
        if not y in dic_lmax.keys():
            dic_lmax[y] = x
        else:
            dic_lmax[y] = max(dic_lmax[y], x)


for k in dic_rmin:
    if not k in dic_lmax: continue
    if dic_rmin[k] < dic_lmax[k]:
        end('Yes')

print('No')
