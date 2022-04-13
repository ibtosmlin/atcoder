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
n, l = map(int, input().split())
s = []
for _ in range(n):
    si = input()
    now = 0
    for c in si:
        now += 1 << (ord(c) - ord('a'))
    s.append(now)

ret = 0
for i in range(1, 1<<n):
    bc = bin(i).count('1')
    uses = (1<<26) - 1
    for j in range(n):
        if i>>j & 1:
            uses &= s[j]
    cnt = pow(bin(uses).count('1'), l, mod1)
    if bc%2 == 1:
        ret += cnt
    else:
        ret -= cnt
    ret %= mod1


print(ret)