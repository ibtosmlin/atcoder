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

def compress(points, reverse=False, spacing=False):
    """一次元座標圧縮

    Parameters
    ----------
    points : list
         値のリスト [100,300,50,900,200]

    Returns
    -------
    pos : {50: 0, 100: 1, 200: 2, 300: 3, 900: 4}
    vals : {0: 50, 1: 100, 2: 200, 3: 300, 4: 900}
    """
    pos = {}
    vals = {}
    sx = set(points)
    if spacing:
        for p in points:
            sx.add(p+1)

    for i, xi in enumerate(sorted(set(sx), reverse=reverse)):
        pos[xi] = i
        vals[i] = xi
    sx_cmp = [pos[xi] for xi in sx]
    return pos, vals, sx_cmp

n, k = map(int, input().split())
a = list(map(int, input().split()))

pos, vals, sx_cmp = compress(a)

a2 = [pos[ai] for ai in a]

minpos = [-1] * len(pos)
for i in range(k, n)[::-1]:
    minpos[a2[i]] = i

now = INF
for i in range(len(pos))[::-1]:
    if minpos[i] != -1:
        now = min(now, minpos[i])
    minpos[i] = now

ret = INF
for i in range(k):
    if a2[i] != len(pos)-1:
        ret = min(ret, minpos[a2[i] + 1] - i)

print(-1 if ret == INF else ret)
