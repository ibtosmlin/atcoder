# https://atcoder.jp/contests/joi2018yo/tasks/joi2018_yo_d
n = int(input())
l = [int(input()) for _ in range(n)]
rl = [0]
for li in l:
    rl.append(rl[-1] +li)

mx = rl[-1]
mn = min(l)
INF = mx * 2

# dp[i][j]  iで切った場合で、最小がjの最大値の最小値
dp = [[mx*2] * (mx + 1) for _ in range(n+1)]
dp[0][mx] = mx
for i in range(n):
    for j in range(mx+1):
        if dp[i][j] == INF: continue
        for k in range(i+1, n+1):
            # kが次の切れ目
            ll = rl[k] - rl[i]
            if i != 0:
                dp[k][min(ll, j)] = min(dp[k][min(ll, j)], max(dp[i][j], ll))
            else:
                dp[k][min(ll, j)] = min(dp[k][min(ll, j)], ll)

ret = INF
for i in range(1, mx+1):
    mxi = dp[-1][i]
    if mxi >= mx: continue
    ret = min(ret, mxi-i)
print(ret)
