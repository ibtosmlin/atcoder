# https://atcoder.jp/contests/past202012-open/tasks/past202012_m
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
from bisect import bisect_left, bisect_right

n, l = map(int, input().split())
A = list(map(int, input().split())) + [10**18]
RA = [0]
for ai in A:
    RA.append(RA[-1] + ai)

def isok(x):
    dp = [0] * (n+2)
    dp[0] = 1
    dp[1] = -1
    for i in range(n):
        if dp[i]:
            a = bisect_left(RA, RA[i] + x)
            b = bisect_right(RA, RA[i] + l)
            dp[a] += 1
            dp[b] -= 1
        dp[i+1] += dp[i]
    # print(x, dp)
    return dp[n] > 0

ok = 1
ng = l+1

while ng - ok > 1:
    mid = (ng+ok) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid

print(ok)


