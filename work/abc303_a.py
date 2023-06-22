# https://atcoder.jp/contests/abc303/tasks/abc303_a
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
import sys
sys.setrecursionlimit(10001000)
INF1 = float('inf'); INF = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
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
n = int(input())
s = input()
t = input()

def isok(u, v):
    if u == v: return True
    if u == '1' and v == 'l': return True
    if u == '0' and v == 'o': return True
    if v == '1' and u == 'l': return True
    if v == '0' and u == 'o': return True
    return False


for i in range(n):
    if isok(s[i], t[i]): continue
    print('No')
    exit()
print('Yes')