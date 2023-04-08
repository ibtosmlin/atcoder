# https://atcoder.jp/contests/past201912-open/tasks/past201912_o
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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()
def fstr(x): return f'{x:.10f}'
n = int(input())
A = []
nums = set()
for _ in range(n):
    ai = list(map(int, input().split()))
    ai.sort(reverse=True)
    A.append(ai)
    nums |= set(ai)
nums = sorted(list(nums), reverse=True)
rnums = dict()
for i, num in enumerate(nums):
    rnums[num] = i



print(A)
print(nums)
print(rnums)

# i回目まで投げました、今の目はj番目のnums[j]です
# 何を選ぶ x の場合のそれぞれの期待値が一番大きいやつです
# E[j][d] / 6 + 1 = E[j][d]
#