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


def f(n, s):
    l = n//2
    d = n%2
    ret = 0
    for i in range(l):
        u = (ord(s[i])-ord('A'))*pow(26, max(l-i-1+d,0), mod1)
#        print(s, i, u)
        ret += u
        ret %= mod1

    if d:
        ret += ord(s[l])-ord('A')
        if s[:l][::-1] <= s[-l:]:
            ret += 1
    else:
        if s[:l][::-1] <= s[-l:]:
            ret += 1

    return ret%mod1


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(f(n, s))
