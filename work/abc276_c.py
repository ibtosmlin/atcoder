# https://atcoder.jp/contests/abc276/tasks/abc276_c
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
n = int(input())
p = list(map(int, input().split()))
q = p[:]
class Solution(object):
   def prevPermOpt1(self, A):
      n = len(A)
      for left in range(n-2,-2,-1):
         if left == -1:
            return A
         elif A[left]>A[left+1]:
            break
      element = 0
      index = 0
      for right in range(left+1,n):
         if A[right]<A[left] and A[right]>element:
            element = A[right]
            index = right
      temp = A[left]
      A[left] = A[index]
      A[index] = temp
      return A
ob = Solution()

x = ob.prevPermOpt1(p)


for i in range(n):
    if x[i] != q[i]:
        break

f = x[:i+1]
r =x[i+1:]
r.sort(reverse=True)
print(*(f+r))
