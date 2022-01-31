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
s = list(input())
pos = []

mn = n
for ci in range(26):
    nmn = mn
    for i in range(mn)[::-1]:
        if ci == ord(s[i])-ord('a'):
            pos.append(i)
            nmn = i
    mn = nmn



l = 0
id = 0
r = pos[id]
for l in range(n):
    if s[l] > s[r]:
        s[l], s[r] = s[r], s[l]
        l += 1
        id += 1
        r = pos[id]
    elif s[l] == s[r]:
        l += 1
    if l >= r: break
print("".join(s))
