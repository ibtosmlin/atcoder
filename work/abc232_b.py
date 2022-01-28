import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10001000)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()

s = input()
t = input()

d = ord(s[0]) - ord(t[0])
d %= 26

for si, ti in zip(s, t):
    if (ord(si) - ord(ti))%26 != d:
        end('No')


print('Yes')