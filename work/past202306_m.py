# https://atcoder.jp/contests/past15-open/tasks/past202306_m
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
d = sorted(map(int, input().split()))
t = sum(d)
s = t // 2
dp = [False] * (s+1)
dp[0] = True
for di in d:
    for j in range(s)[::-1]:
        if dp[j] and j+di <= s:
            dp[j+di] = True
ret = 10**20
for i in range(s+1):
    if dp[i]:
        ret = min(t - 2*i, ret)
print(ret)