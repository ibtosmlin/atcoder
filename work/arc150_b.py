# https://atcoder.jp/contests/arc150/tasks/arc150_b
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()
def fstr(x): return f'{x:.10f}'

def f(A, B):
    MX = min(A, B)
    ret = A+B
    for k in range(A, 45000):
        x = ((B+k-1) // k) * k
        ret = min(ret, (x-B) + (k-A))
    for k in range(1, 45000):
        A2 = A
        if B > A*k:
            A2 = (B+k-1)//k
        ret = min(ret, A2*k-B+A2-A)
    return ret




t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(f(a, b))