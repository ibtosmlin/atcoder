# https://atcoder.jp/contests/pakencamp-2020-day1/tasks/pakencamp_2020_day1_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import defaultdict
n = int(input())
count = defaultdict(int)
for _ in range(n):
    k = int(input())
    for nm in input().split():
        count[nm] += 1

ret = 0
for k, v in count.items():
    if v == n:
        ret += 1
print(ret)
