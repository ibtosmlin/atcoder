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
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'
def end(r=-1): print(r); exit()
from bisect import *

n = int(input())
a = list(map(int, input().split()))
dic = d = defaultdict(list)
for i, ai in enumerate(a):
    dic[ai].append(i+1)

q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    if not x in dic:
        print(0)
    else:
        que = dic[x]
        l -= 1
        posr = bisect_right(que, r)
        posl = bisect_right(que, l)
        print(posr - posl)
