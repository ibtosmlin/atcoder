import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'


n = int(input())
memo = dict()

def f(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 1
    memo[n] = f(n-1) + f(n-2)
    return memo[n]

print(f(n))