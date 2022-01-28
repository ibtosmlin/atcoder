import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=26->'z'


n, q = map(int, input().split())

class matrix:
    def __init__(self, r, c) -> None:
        self.r = r
        self.c = c
        self.mat = [[None] * c for _ in range(r)]
        self.rot = 0
        self.v_revesed = False
        self.h_revesed = False


    def rot90(n:int, x:tuple)->tuple:
        i, j = x
        return (j, n-1-j)

    def h_rev(n:int, x:tuple)->tuple:
        i, j = x
        return (i, n-1-j)

    def v_rev(n:int, x:tuple)->tuple:
        i, j = x
        return (n-1-i, j)


def get_reverse(n, x y):


rot = 0
v_rev = False
h_rev = False

for _ in range(q):
    query = input().split()
    if query[0] == '2':
        if query[1] == 'A':
            rot += 1
        else:
            rot -= 1
        rot %= 4
    elif query[0] == '3':
        if query[1] == 'A' ^ rot%2==0:
            v_rev = not v_rev
        else:
            h_rev = not h_rev
