# https://atcoder.jp/contests/cpsco2019-s1/tasks/cpsco2019_s1_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from itertools import *

N, K = map(int, input().split())
A = list(map(int, input().split()))
C = list(combinations(range(N), K))   # 順列(nPr)
INF = 10**10

def cnt(x):
    ret = 0
    for i in range(10)[::-1]:
        coini = pow(10, i)
        for coinj in [5, 1]:
            coin = coini * coinj
            ret += x//coin
            x = x%coin
    return ret

ret = INF
for pi in C:
    price = 0
    for pij in pi:
        price += A[pij]
    ret = min(ret, cnt(price))

print(ret)
