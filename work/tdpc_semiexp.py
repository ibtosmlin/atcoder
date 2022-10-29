mod = 10 ** 9 + 7
n, k = map(int, input().split())
dp = [0] * (n+2)
dp[0] = 1

m = 0
for i in range(n+2):
    if i > 1:
        dp[i] = m
    m += dp[i]
    if i >= k-1:
        m -= dp[i-k]
    m %= mod
print((dp[-1]-dp[-2])%mod)
