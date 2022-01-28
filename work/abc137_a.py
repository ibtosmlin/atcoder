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

a, b = map(int, input().split())
ret = -100000
ret = max(ret, a*b)
ret = max(ret, a-b)
ret = max(ret, a+b)










print(ret)

# print('Yes' if ret else 'No')
# print(-1 if ret == INF else ret)
# print('\n'.join(ret))
# print('\n'.join(map(str, ret)))
