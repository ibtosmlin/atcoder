import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
from bisect import bisect
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
b = [0] + list(accumulate(a))

def check(x):
    u = bisect(b, b[x]+p) - 1
    if u == n+1: return False
    if b[u] != b[x]+p: return False
    u = bisect(b, b[x]+p+q) - 1
    if u == n+1: return False
    if b[u] != b[x]+p+q: return False
    u = bisect(b, b[x]+p+q+r) - 1
    if u == n+1: return False
    if b[u] != b[x]+p+q+r: return False
    return True


for i in range(n):
    if check(i):
        end('Yes')
end('No')
