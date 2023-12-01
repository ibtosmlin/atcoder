# https://atcoder.jp/contests/abc143/tasks/abc143_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
L = list(map(int, input().split()))
L.sort()
from bisect import bisect_left

# a < b < c
#  a < b + c ok
#  b < c + a ok
#  c < a + b ?
ret = 0
for i in range(n-2):
    a = L[i]
    for j in range(i+1, n-1):
        b = L[j]
        c = a + b
        ret += bisect_left(L, c) - j - 1
print(ret)