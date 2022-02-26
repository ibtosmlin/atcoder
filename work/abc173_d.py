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
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

que = []
heapify(que)
heappush(que, -a[0])

ret = 0
for i in range(1, n):
    x = heappop(que)
    ret += -x
    heappush(que, -a[i])
    heappush(que, -a[i])

print(ret)