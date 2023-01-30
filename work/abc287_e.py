# https://atcoder.jp/contests/abc287/tasks/abc287_e
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
n = int(input())
S = [(input(), i) for i in range(n)]
S.sort()

def lcp(u, v):
    ret = 0
    for i in range(min(len(u), len(v))):
        if u[i] != v[i]:
            break
        ret += 1
    return ret

ret = [0] * n
for i in range(n-1):
    sp0, pos0 = S[i]
    sp1, pos1 = S[i+1]
    l = lcp(sp0, sp1)
    ret[pos0] = max(ret[pos0], l)
    ret[pos1] = max(ret[pos1], l)

print('\n'.join(map(str, ret)))