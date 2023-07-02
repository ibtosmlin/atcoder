# https://atcoder.jp/contests/abc308/tasks/abc308_b
from itertools import *
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys; sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i, base='a'): return chr(ord(base) + i%26)    # i=0->'a', i=25->'z'
def alpind(a, base='a'): return ord(a)-ord(base)
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def printyes(ret:bool): print('Yes' if ret else 'No')
def end(r=-1): exit(print(r))
n ,m =map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))
pl = p[0]
p = p[1:]

u = dict()
for di, pi in zip(d, p):
    u[di] = pi

ret = 0
for ci in c:
    if ci in u:
        ret += u[ci]
    else:
        ret += pl
print(ret)
