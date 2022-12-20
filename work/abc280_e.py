# https://atcoder.jp/contests/abc280/tasks/abc280_e
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)

n, p = map(int, input().split())
dp = [0] * (n+1)
dp[1] = 1
pp = p * modinv(100, mod1) % mod1
qq = (1 - pp) % mod1

for i in range(2, n+1):
    dp[i] = (1 + dp[i-1] * qq + dp[i-2] * pp)%mod1

print(dp[n])
