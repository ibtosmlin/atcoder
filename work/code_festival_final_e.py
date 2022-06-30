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
r = list(map(int, input().split()))
udp = [[0]*(1+n) for _ in range(n+1)]
ddp = [[0]*(1+n) for _ in range(n+1)]
for i in range(n):
    # r[i]初めて使う
    udp[i+1][i+1] = 1
    ddp[i+1][i+1] = 1
    for j in range(1, i+1):
        udp[i+1][j] = udp[i][j] #使わない
        ddp[i+1][j] = ddp[i][j] #使わない
        # r[i]使う 最後に使ったのがr[j-1]
        if r[i] > r[j-1]:
            ddp[i+1][i+1] = max(udp[i][j] + 1, ddp[i+1][i+1])
        elif r[i] < r[j-1]:
            udp[i+1][i+1] = max(ddp[i][j] + 1, udp[i+1][i+1])

ret = 0
for x in udp[-1]:
    if x >= 3:
        ret = max(ret, x)
for x in ddp[-1]:
    if x >= 3:
        ret = max(ret, x)
print(ret)
