# https://atcoder.jp/contests/arc156/tasks/arc156_b
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()



#####################################
# nCr % 10**9+7
#####################################
mod, lim = 998244353, 10**6                   # mod素数, 出力の制限
g1, g2 = [[1]*(lim+1) for _ in range(2)]    # ！と逆元tbl
for i in range(2, lim + 1):
    g1[i] = g1[i-1] * i % mod
g2[-1] = pow(g1[-1], mod-2, mod)
for i in range(lim, 0, -1):
    g2[i-1] = g2[i] * i % mod

def fac(n): return g1[n]
def facinv(n): return g2[n]
def nCr(n, r):
    """nCr
    n個のものからr個選ぶ
    """
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return fac(n) * facinv(r) * facinv(n-r) % mod


n, k = map(int, input().split())
a = list(map(int, input().split()))
MX = 10 ** 6
isin = [0] * MX
for ai in a:
    isin[ai] = 1
for i in range(1, MX):
    isin[i] += isin[i-1]

def need(i):
    if i == 0: return 1
    return i - isin[i-1] + 1

ret = 0
for i in range(n+k+1):
    u = k - need(i)
    if u < 0: continue
    if u == 0:
        ret += 1
    else:
        ret += nCr(u+i, i)
        ret %= 998244353

print(ret)



def z_algo(S):
    N = len(S)
    A = [0]*N
    i = 1; j = 0
    A[0] = l = len(S)
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A

s = 'ippisisim'
s = s[::-1]
ret = z_algo(s)
for i in range(len(s)):
    print(i, ret[i], s, s[i:])


def z_algo(S):
    N = len(S)
    A = [0]*N
    i = 1; j = 0
    A[0] = l = len(S)
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A

s = 'ippisisim'
ret = z_algo(s)
for i in range(len(s)):
    print(i, ret[i], s, s[i:])
