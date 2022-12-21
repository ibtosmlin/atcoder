# https://atcoder.jp/contests/abc281/tasks/abc281_b
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
s=input()

if len(s) != 8:
    print('No')
    exit()
if not s[0] in ALPS:
    print('No')
    exit()
if not s[-1] in ALPS:
    print('No')
    exit()
u = s[1:7]
for ui in u:
    if not ui in '0123456789':
        print('No')
        exit()

if int(u) <= 99999:
    print('No')
    exit()
if int(u) >= 1000000:
    print('No')
    exit()
print('Yes')
