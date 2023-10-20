# https://atcoder.jp/contests/abc044/tasks/arc060_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [[0] * 3000 for _ in range(n+1)]
dp[0][0] = 1

for xi in x:
    ndp = [[0] * 3000 for _ in range(n+1)]
    for i in range(n+1):
        for j in range(3000):
            ndp[i][j] += dp[i][j]
            if i+1 <= n and xi+j < 3000:
                ndp[i+1][xi+j] += dp[i][j]
    dp = ndp
ret = 0
for c in range(n+1):
    for s in range(3000):
        if c * a == s:
            ret += dp[c][s]
print(ret-1)