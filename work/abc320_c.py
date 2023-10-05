# https://atcoder.jp/contests/abc320/tasks/abc320_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from itertools import *
P = list(permutations(range(3)))   # 順列(nPr)

m = int(input())
s = [input() * 3 for _ in range(3)]

INF = 10**10

def find(ss, s):
    t = -1
    for i in range(3):
        t = ss[i].find(s, t+1)
        if t == -1: return INF
    return t

ret = INF

for i in range(10):
    si = str(i)
    for p in P:
        ret = min(ret, find((s[p[0]], s[p[1]], s[p[2]]), si))

print(-1 if ret == INF else ret)
