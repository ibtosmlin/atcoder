import sys
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10001000)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def end(r=-1): print(r); exit()


def f(x):
    return x**2+x*2+3

def g(t):
     return f(f(f(t)+t)+f(f(t)))

t = int(input())
print(g(t))