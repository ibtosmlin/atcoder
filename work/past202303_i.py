# https://atcoder.jp/contests/past202303-open/tasks/past202303_i
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
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): exit(print(r))
hands = []
n = int(input())
x = list(input())
sx = []
for i in range(5):
    for j in range(i):
        for k in range(j):
            sx.append([alpind(x[i]), alpind(x[j]), alpind(x[k])])

for i in range(n):
    s = input()
    for j in range(4):
        for k in range(j):
            uset = [alpind(s[j]), alpind(s[k])]
            for sxi in sx:
                c = Counter(uset+sxi)
                m = 30
                r = 0
                for ky, v in c.items():
                    if r <= v:
                        if m > ky:
                            m = ky
                            r = v
                heappush(hands, (-r, m, i))

x = heappop(hands)
print(x[-1]+1)

# 5C3 = 20
# 4C2 = 6
# 20 * 6
