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
n, q = map(int, input().split())

pos = [i for i in range(n)]
lis = [i for i in range(n)]

for _ in range(q):
    x = int(input())
    x -= 1
    px = pos[x]
    #x:pxにいる
    if px == n-1:
        py = px - 1
    else:
        py = px + 1
    y = lis[py]
    #y:pyとスイッチ

    pos[x] = py
    pos[y] = px
    lis[px] = y
    lis[py] = x

ret = [i+1 for i in lis]
print(*ret)