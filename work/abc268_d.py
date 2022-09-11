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
n, m = map(int, input().split())

sl = [input() for _ in range(n)]
tl = set(input() for _ in range(m))

if n == 1:
    s = sl[0]
    if s not in tl and  3 <= len(s) <= 16:
        end(s)
    else:
        end(-1)

x = 16 - (len(''.join(sl)) + n-1)

for pi in permutations(sl):
    ret = '_'.join(pi)
    if 3 <= len(ret) <= 16 and not ret in tl:
        end(ret)

    for xi in range(1, x+1):
        CR = list(combinations_with_replacement(range(n-1), xi))
        for cri in CR:
            ret2 = [1] * (n-1) + [0]
            for crii in cri:
                ret2[crii] += 1
            ret2 = ['_' * i for i in ret2]
            ret = []
            for i in range(n):
                ret.append(pi[i])
                ret.append(ret2[i])
            ret = ''.join(ret)
            if 3 <= len(ret) <= 16 and not ret in tl:
                end(ret)

end(-1)
