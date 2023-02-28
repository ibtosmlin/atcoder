# https://atcoder.jp/contests/abc291/tasks/abc291_d
mod = 1000000007; mod1 = 998244353
n = int(input())
dp = [[0] * 2 for _ in range(n+1)]
dp[0][0] = 1
now = [-1, -1]
for i in range(n):
    nxt = list(map(int, input().split()))
    for j in range(2):
        for k in range(2):
            if now[j] != nxt[k]:
                dp[i+1][k] += dp[i][j]
                dp[i+1][k] %= mod1
    now = nxt
print(sum(dp[-1])%mod1)