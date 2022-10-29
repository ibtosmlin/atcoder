# https://atcoder.jp/contests/abc275/tasks/abc275_e
mod = 1000000007; mod1 = 998244353
def modinv(x, mod): return pow(x, mod - 2, mod)
n, m, k = map(int, input().split())
minv = modinv(m, mod1)
dp = [0] * n
dp[0] = 1
ret = 0
for i in range(k):
    ndp = [0] * n
    for fm in range(n):
        np = (dp[fm] * minv) % mod1
        for u in range(1, m+1):
            to = fm + u
            if to > n: to = n - (to - n)
            if to == n:
                ret += np
                ret %= mod1
            else:
                ndp[to] += np
                ndp[to] %= mod1
    dp, ndp = ndp, dp
print(ret)
