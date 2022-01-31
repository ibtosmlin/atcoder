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
n = int(input())
a = []
for i in range(2*n):
    b = list(map(int, input().split()))
    a.append([0]*(i+1)+b)


ret = 0

def dfs(bit, xo):
    global ret
    if bit == 0:
        ret = max(ret, xo)
        return
    for i in range(2*n):
        if bit >> i & 1 != 0: break
    for j in range(i+1, 2*n):
        if bit >> j & 1 == 0: continue
        nxtxo = xo ^ a[i][j]
        nxtbit = bit - (1<<i) - (1<<j)
        dfs(nxtbit, nxtxo)

dfs((1<<(2*n))-1, 0)
print(ret)