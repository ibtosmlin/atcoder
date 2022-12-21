# https://atcoder.jp/contests/abc281/tasks/abc281_d


n, k, d = map(int, input().split())
a = list(map(int, input().split()))
dp = [[-1] * d for _ in range(k+1)]
dp[0][0] = 0
for i, ai in enumerate(a):
    ndp = [[-1] * d for _ in range(k+1)]
    for u in range(k+1):
        for j in range(d):
            if dp[u][j] == -1: continue
            ndp[u][j] = max(ndp[u][j], dp[u][j])
            if u+1 <= k:
                nxt = (j+ai)%d
                ndp[u+1][nxt] = max(ndp[u+1][nxt], dp[u][j]+ai)
    dp = ndp
print(dp[k][0])
