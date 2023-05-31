def end(r): print(r); exit()
mod = 998244353

n, d = map(int, input().split())
A = list(map(int, input().split()))
D = 2 * d + 1

dp = [[0] * (1<<D) for _ in range(n+1)]
dp[0][0] = 1

for i, ai in enumerate(A):
    ii = i+1
    di = ai - ii
    dsi = di + d
    if ai != -1:
        if abs(di) > d:
            end(0)
        else:
            for j in range(1<<D):
                next = j >> 1
                if next >> dsi & 1: continue
                dp[i+1][next | 1<<dsi] += dp[i][j]
                dp[i+1][next | 1<<dsi] %= mod
    else:
        for j in range(1<<D):
            next = j >> 1
            for k in range(D):
                if ii + k - d <= 0 or ii + k - d > n:continue
                if next >> k & 1: continue
                dp[i+1][next | 1<<k] += dp[i][j]
                dp[i+1][next | 1<<k] %= mod

print(max(dp[-1]))
# for dpi in dp: print(dpi)