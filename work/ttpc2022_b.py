# https://atcoder.jp/contests/ttpc2022/tasks/ttpc2022_b
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
n, x = map(int, input().split())
a = list(map(int, input().split()))
PS = [list(permutations(range(i))) for i in range(5)]

ra = [a[-1]]
for ai in a[:-1][::-1]:
    ra.append(ra[-1]+ai)
ra = ra[::-1]
print(ra)


memo = dict()
def nums(s):
    if s < 0: return set()
    if s in memo: return memo[s]
    s = str(s)
    ret = set()
    for pi in PS[len(s)]:
        nw = [s[j] for j in pi]
        ret.add(int(''.join(nw)))
    memo[s] = ret
    return ret

dp = defaultdict(int)
for u in nums(x):
    dp[u] = 0

for i, (ai, ri) in enumerate(zip(a, ra)):
    ndp = defaultdict(int)
    for k, v in dp.items():
        if k >= ri: 
        ndp[k] = max(ndp[k], v)
        for nk in nums(k-ai):
            ndp[nk] = max(v + 1, ndp[nk])
    dp = ndp

print(max(dp.values()))