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
n = int(input())
s = list(map(int, list(input())))
w = list(map(int, input().split()))

sw = []
for i in range(n):
    sw.append((w[i], s[i]))
sw.sort()
z = []
for i in range(n):
    if sw[i][1] == 0:
        z.append(1)
    else:
        z.append(0)
for i in range(1,n):
    z[i] += z[i-1]

p = []
for i in range(n):
    if sw[i][1] == 1:
        p.append(1)
    else:
        p.append(0)
for i in range(1, n)[::-1]:
    p[i-1] += p[i]

ret = max(p[0], z[-1])
for i in range(1, n):
    if sw[i][0] == sw[i-1][0]: continue
    ret = max(ret, p[i]+z[i-1])


print(ret)