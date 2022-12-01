# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bv
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
# ma: nxm
# mb: mxk
# returns nxk - matrix

def prod(ma, mb):
    n_a = len(ma)
    m_a = len(ma[0])
    n_b = len(mb)
    m_b = len(mb[0])
    if n_a*m_a*n_b*m_b == 0: return 0
    if m_a != n_b: return 0

    ret = []
    for i in range(n_a):
        rw = []
        for j in range(m_b):
            c = 0
            for k in range(m_a):
                c += ma[i][k]*mb[k][j]
            rw.append(c)
        ret.append(rw)
    return ret

def powmat(ma, k):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for _ in range(k):
        if k & 1:
            ret = prod(ret, ma)
        ma = prod(ma, ma)
        k >>= 1
        if k == 0: break
    return ret

q = int(input())
for _ in range(q):
    x, y, z, t = input().split()
    x, y, z = float(x), float(y), float(z)
    t = int(t)
    matA = [[1-x, y, 0],[0, 1-y, z],[x,0,1-z]]
    ret = powmat(matA, t)
    ret = ["{:.15f}".format(sum(ri)) for ri in ret]
    print(*ret)
