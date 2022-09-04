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

s = input()
s = "x" + s
if s[1] == '1':
    end('No')
x = [1] * 7
if s[7] == "0": x[0] = 0
if s[4] == "0": x[1] = 0
if s[2] == "0" and s[8] == "0": x[2] = 0
if s[5] == "0": x[3] = 0
if s[3] == "0" and s[9] == "0": x[4] = 0
if s[6] == "0": x[5] = 0
if s[10] == "0": x[6] = 0

xs = ''.join(map(str, x))
#print(xs)
if '101' in xs:
    end('Yes')
if '1001' in xs:
    end('Yes')
if '10001' in xs:
    end('Yes')
if '100001' in xs:
    end('Yes')
if '1000001' in xs:
    end('Yes')

end('No')
