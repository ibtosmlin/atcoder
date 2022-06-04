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
n, k = map(int, input().split())
s = [[0]*26 for _ in range(n)]
for i in range(n):
    si = input()
    for sii in si:
        s[i][ord(sii)-ord('a')] += 1

ret = 0
for i in range(1<<n):
    nw = 0
    for l in range(26):
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                cnt += s[j][l]
        if cnt == k:
            nw += 1
    ret = max(nw, ret)
print(ret)