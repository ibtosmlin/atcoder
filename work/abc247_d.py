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

q = int(input())
que = deque()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        que.append((query[1], query[2]))
    else:
        c = query[1]
        ret = 0
        while c > 0:
            xi, ci = que.popleft()
            use = min(c, ci)
            ret += use * xi
            c -= use
            ci -= use
        if ci != 0:
            que.appendleft((xi, ci))
        print(ret)


