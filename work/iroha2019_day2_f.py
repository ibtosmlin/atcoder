# https://atcoder.jp/contests/iroha2019-day2/tasks/iroha2019_day2_f
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

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

def bit(a1, a2, b1, b2, c1, c2):
    ret = a1
    ret = ret*11 + a2
    ret = ret*11 + b1
    ret = ret*11 + b2
    ret = ret*11 + c1
    ret = ret*11 + c2
    return ret

first = (a1 + a2 + b1 + b2 + c1 + c2)%2

memo = dict()
memo[0] = 0
def dfs(x):
    if x in memo: return memo[x]
    dx = x
    dx, c2 = divmod(dx, 11)
    dx, c1 = divmod(dx, 11)
    dx, b2 = divmod(dx, 11)
    dx, b1 = divmod(dx, 11)
    a1, a2 = divmod(dx, 11)
    turn = (a1 + a2 + b1 + b2 + c1 + c2)%2
    if turn == first:
        ans = []
        # 物理
        # choose A
        if a1 + a2 > 0:
            ra = 0
            if a1 >= 1:
                ra += dfs(bit(a1-1, a2, b1, b2, c1, c2)) * a1
            if a2 >= 1:
                ra += dfs(bit(a1, a2-1, b1, b2, c1, c2)) * a2
            ra += 100*a1+50*a2
            ra /= a1 + a2
            ans.append(ra)
        if b1 + b2 > 0:
            rb = 0
            if b1 >= 1:
                rb += dfs(bit(a1, a2, b1-1, b2, c1, c2)) * b1
            if b2 >= 1:
                rb += dfs(bit(a1, a2, b1, b2-1, c1, c2)) * b2
            rb += 100*b1+50*b2
            rb /= b1 + b2
            ans.append(rb)
        if c1 + c2 > 0:
            rc = 0
            if c1 >= 1:
                rc += dfs(bit(a1, a2, b1, b2, c1-1, c2)) * c1
            if c2 >= 1:
                rc += dfs(bit(a1, a2, b1, b2, c1, c2-1)) * c2
            rc += 100*c1+50*c2
            rc /= c1 + c2
            ans.append(rc)
        ret = max(ans)
    else:
        ans = []
        # 物理
        # choose A
        if a1 + a2 > 0:
            ra = 0
            if a1 >= 1:
                ra += dfs(bit(a1-1, a2, b1, b2, c1, c2)) * a1
            if a2 >= 1:
                ra += dfs(bit(a1, a2-1, b1, b2, c1, c2)) * a2
#            ra += 100*a1+50*a2
            ra /= a1 + a2
            ans.append(ra)
        if b1 + b2 > 0:
            rb = 0
            if b1 >= 1:
                rb += dfs(bit(a1, a2, b1-1, b2, c1, c2)) * b1
            if b2 >= 1:
                rb += dfs(bit(a1, a2, b1, b2-1, c1, c2)) * b2
#            rb += 100*b1+50*b2
            rb /= b1 + b2
            ans.append(rb)
        if c1 + c2 > 0:
            rc = 0
            if c1 >= 1:
                rc += dfs(bit(a1, a2, b1, b2, c1-1, c2)) * c1
            if c2 >= 1:
                rc += dfs(bit(a1, a2, b1, b2, c1, c2-1)) * c2
#            rc += 100*c1+50*c2
            rc /= c1 + c2
            ans.append(rc)
        ret = min(ans)
    memo[x] = ret
    return ret

print(dfs(bit(a1, a2, b1, b2, c1, c2)))
#print(memo)