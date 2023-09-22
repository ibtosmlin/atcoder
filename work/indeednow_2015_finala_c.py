# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    a, b, c, w = map(int, input().split())
    dp[a][b][c] = max(w, dp[a][b][c])

for a in range(101):
    for b in range(101):
        for c in range(101):
            if a and b and c:
                dp[a][b][c] = max(dp[a][b][c], dp[a-1][b][c], dp[a][b-1][c], dp[a][b][c-1])
            elif a and b:
                dp[a][b][c] = max(dp[a][b][c], dp[a-1][b][c], dp[a][b-1][c])
            elif b and c:
                dp[a][b][c] = max(dp[a][b][c], dp[a][b-1][c], dp[a][b][c-1])
            elif c and a:
                dp[a][b][c] = max(dp[a][b][c], dp[a-1][b][c], dp[a][b][c-1])
            elif a:
                dp[a][b][c] = max(dp[a][b][c], dp[a-1][b][c])
            elif b:
                dp[a][b][c] = max(dp[a][b][c], dp[a][b-1][c])
            elif c:
                dp[a][b][c] = max(dp[a][b][c], dp[a][b][c-1])

for _ in range(m):
    a, b, c = map(int, input().split())
    print(dp[a][b][c])
