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
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]


def rotate(X):
    X = X[::-1]
    return [list(x) for x in zip(*X)]

def trans(X):
    return [list(x) for x in zip(*X)]

def offset(X):
    i = 0
    while not "#" in X[i]:
        i += 1
    j = 0
    X_ = trans(X)
    while not "#" in X_[j]:
        j += 1
    ret = [['.'] * n for _ in range(n)]
    for ik in range(i, n):
        for jk in range(j, n):
            ret[ik-i][jk-j] = X[ik][jk]
    return ret

t = offset(t)

if offset(s) == t: end('Yes')
s = rotate(s)
if offset(s) == t: end('Yes')
s = rotate(s)
if offset(s) == t: end('Yes')
s = rotate(s)
if offset(s) == t: end('Yes')
end('No')
