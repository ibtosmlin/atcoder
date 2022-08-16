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
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
h, w = map(int, input().split())
r, c = map(int1, input().split())
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
flag = ["^.", "v.", "<.", ">."]

g = [input() for _ in range(h)]

que = deque()
seen = [[[-1] * 4 for __ in range(w)] for _ in range(h)]

que.append((r, c))
seen[r][c] = [True] * 4

while que:
    ch, cw = que.popleft()
    for i, (dh, dw) in enumerate(direc):
        nh, nw = ch + dh, cw + dw
        if not (0 <= nh < h and 0 <= nw < w): continue
        if seen[nh][nw][i] != -1: continue
        #print(nh, nw, ch, cw)
        if g[nh][nw] in flag[i]:
            que.append((nh, nw))
            seen[nh][nw][i] = True
            #print('A')
        else:
            seen[nh][nw][i] = False
            #print('B')

ret = [["#"] * w for _ in range(h)]
for ch in range(h):
    for cw in range(w):
        if g[ch][cw] == '#':
            ret[ch][cw] = '#'
        else:
            for i in range(4):
                if seen[ch][cw][i] == 1:
                    ret[ch][cw] = 'o'
                    break
            else:
                ret[ch][cw] = 'x'
for ri in ret:
    print(''.join(ri))