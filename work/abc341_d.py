# https://atcoder.jp/contests/abc341/tasks/abc341_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
int1=lambda x: int(x) - 1

import math

n, m, k = map(int, input().split())
nm = math.lcm(n, m)

def count(x):
    return x // n + x // m - x // nm * 2

r = 10**18 + 1
l = 0
while r-l>1:
    mid = (r+l) // 2
    if count(mid) >= k:
        r = mid
    else:
        l = mid
print(r)
