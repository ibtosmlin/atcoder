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
n = int(input())

s = input()

if not 'p' in s:
    end(s)

mx = s[:]

for i in range(n):
    for j in range(i, n):
        ti = s[i:j].translate(str.maketrans({'p':'d', 'd': 'p'}))
        mx = min(mx, s[:i] + ti[::-1] + s[j:])


end(mx)






bs = 0
for i, si in enumerate(s[::-1]):
    if si == "p":
        bs += 1 << i
        l = i

m = bs.bit_length()
mx = bs
print(bin(bs))
for i in range(1,m+1):
    x = ((1 << i) - 1) << (m - i)
    print(bin(bs & x))
