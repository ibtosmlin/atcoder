# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_z
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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])



##############################
# 素数出力 O(n**0.5)
# n <= 10**5
##############################
def get_primes(n:int) -> list:
# n以下の素数列挙
    n += 1
    IsPrime = [True] * n
    IsPrime[0], IsPrime[1] = False, False
    for p in range(n):
        if not IsPrime[p]: continue
        for j in range(p*2, n, p):
            IsPrime[j] = False
    ret = [p for p in range(n) if IsPrime[p]]
    return ret


q = int(input())
x = [int(input()) for _ in range(q)]
mx = max(x) + 1
ps = set(get_primes(mx))
#print(ps)
for xi in x:
    print('Yes' if xi in ps else 'No')
