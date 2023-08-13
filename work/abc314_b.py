# https://atcoder.jp/contests/abc314/tasks/abc314_b
from itertools import *
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(10001000)
def input(): return sys.stdin.readline().rstrip()
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i, base='a'): return chr(ord(base) + i%26)    # i=0->'a', i=25->'z'
def alpind(a, base='a'): return ord(a)-ord(base)
def modinv(x, mod): return pow(x, mod - 2, mod)
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def sqrt(x):
    r = int(x**0.5) - 3
    while (r+1)*(r+1) <= x: r += 1
    return r
def end(r=-1): exit(print(r))
n = int(input())
bet = [[] for _ in range(100)]
for i in range(n):
    c = int(input())
    a = list(map(int, input().split()))
    for ai in a:
        bet[ai].append((c, i+1))
x = int(input())
bet[x].sort()
if len(bet[x]) == 0:
    end(0)
else:
    ret = []
    c = bet[x][0][0]
    for ci, ui in bet[x]:
        if c == ci:
            ret.append(ui)
print(len(ret))
print(*ret)
