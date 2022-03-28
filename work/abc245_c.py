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

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ok_a = True
ok_b = True

for i in range(1, n):
    if abs(a[i] - a[i-1])<=k and ok_a:
        new_ok_a = True
    elif abs(a[i] - b[i-1])<=k and ok_b:
        new_ok_a = True
    else:
        new_ok_a = False

    if abs(b[i] - a[i-1])<=k and ok_a:
        new_ok_b = True
    elif abs(b[i] - b[i-1])<=k and ok_b:
        new_ok_b = True
    else:
        new_ok_b = False

    ok_a = new_ok_a
    ok_b = new_ok_b

if ok_a or ok_b:
    end('Yes')
else:
    end('No')