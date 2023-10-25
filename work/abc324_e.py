# https://atcoder.jp/contests/abc324/tasks/abc324_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from bisect import bisect_left

n, T = input().split()
n = int(n)
Ss = [input() for _ in range(n)]
lt = len(T)
rT = T[::-1]

def check(s, t):
    ti = 0
    for si in range(len(s)):
        if s[si] == t[ti]: ti += 1
        if ti == lt: break
    return ti

L = []
R = []
for s in Ss:
    L.append(check(s, T))
    R.append(check(s[::-1], rT))

R.sort()
ret = 0
for li in L:
    ret += n - bisect_left(R, lt-li)
print(ret)