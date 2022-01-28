import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10001000)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()
x, y = map(int, input().split('x'))
print(x*y)
