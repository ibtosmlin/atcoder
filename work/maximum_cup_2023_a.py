# https://atcoder.jp/contests/maximum-cup-2023/tasks/maximum_cup_2023_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

from collections import Counter
n = int(input())
a = list(map(int, input().split()))
A = Counter(a)
ret = 0
for v in A.values():
    ret += v * (v-1) // 2
print(ret)