# https://atcoder.jp/contests/joi2024yo1c/tasks/joi2024_yo1c_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

from collections import Counter
k = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
A = Counter(a)
B = Counter(b)

ret = 0

for ai, ca in A.items():
    for bj, cb in B.items():
        if ai + k == bj:
            ret += ca*cb
print(ret)
