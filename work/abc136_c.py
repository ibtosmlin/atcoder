# https://atcoder.jp/contests/abc136/tasks/abc136_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

n = int(input())
H = list(map(int, input().split()))

dp = [[False] * 2 for _ in range(n+1)]
dp[0][0] = True
now = 0
for i in range(n):
    if dp[i][0]:
        if now <= H[i]:
            dp[i+1][0] = True
        if now <= H[i] - 1:
            dp[i+1][1] = True
    if dp[i][1]:
        if now - 1 <= H[i]:
            dp[i+1][0] = True
        if now - 1 <= H[i] - 1:
            dp[i+1][1] = True
    now = H[i]

if dp[-1][0] or dp[-1][1]:
    print('Yes')
else:
    print('No')
