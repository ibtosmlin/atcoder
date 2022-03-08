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
s = [list(input()) for _ in range(n)]

direc = {(1, 0), (0, 1), (1, 1), (1, -1)}

for ch in range(n):
    for cw in range(n):
        for dh, dw in direc:
            cnt = 0
            for i in range(6):
                nh, nw = ch + dh*i, cw + dw*i
                if not (0 <= nh < n and 0 <= nw < n):
                    cnt = 4
                    break
                if s[nh][nw] == '.':
                    cnt += 1
            if cnt <=2:
                end('Yes')

end('No')