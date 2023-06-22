# https://atcoder.jp/contests/abc303/tasks/abc303_e
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
dim = [0] * n
edges = []
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edges.append((a, b))
    dim[a] += 1
    dim[b] += 1

ret = []
centers = set()
for i in range(n):
    if dim[i] > 2:
        centers.add(i)
        ret.append(dim[i])

G = [[] for _ in range(n)]

centers2 = set()
for a, b in edges:
    if a in centers or b in centers:
        centers2.add(a)
        centers2.add(b)


nodes = set()
for a, b in edges:
    if a in centers2 or b in centers2: continue
    nodes.add(a)
    nodes.add(b)

# print(nodes)
x = len(nodes)//3
ret = [2] * x + ret
ret.sort()
print(*ret)

# print(centers)
# print(G)