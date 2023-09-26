# https://atcoder.jp/contests/pakencamp-2021-day2/tasks/pakencamp_2021_day2_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
from collections import Counter
n, m = map(int, input().split())
A = list(map(int, input().split()))
CA = Counter(A)
mx = max(CA.values())
mn = mx
for i in range(1, m+1):
    if i in CA:
        mn = min(mn, CA[i])
    else:
        mn = 0
        break
print(mn, mx)