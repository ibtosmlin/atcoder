# https://atcoder.jp/contests/arc153/tasks/arc153_a
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
# s1,s2,s3,s4,s5,s6,s7,s8,s9
# s1,s3,s4,s5,s7,s8

# s1 : 1 - 9
# s3 : 0 - 9
# s4 : 0 - 9
# s5 : 0 - 9
# s7 : 0 - 9
# s8 : 0 - 9

# 100000 - 999999
# 100000 + n - 1
n += 99999
n = str(n)

print(n[0] + n[0] + n[1] + n[2] + n[3] + n[3] + n[4] + n[5] + n[4])
