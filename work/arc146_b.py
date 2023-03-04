# https://atcoder.jp/contests/arc146/tasks/arc146_b
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
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()
n, m, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(30):
    d = 30 - i
    x = 1 << d
    a.sort(reverse=True)
    ne = [max(0,x - ai) for ai in a[:k]]
    need = sum(ne)
    print(d, a, ne, need)
    if need <= m:
        m -= need
        ret = x + min(m//k, x - 1)
        break
    else:
        for i in range(n):
            a[i] &= ~x
print(ret)

