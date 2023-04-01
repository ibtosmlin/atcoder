N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w, m = map(int, input().split())
    now = 1
    while m:
        use = min(now, m)
        items.append([v*use, w*use])
        m -= use
        now *= 2

dp = [-1] * (W+1)
dp[0] = 0

for v, w in items:
    ndp = [-1] * (W+1)
    for i in range(W+1):
        ndp[i] = dp[i]
        if i-w>=0 and dp[i-w] != -1:
            ndp[i] = max(ndp[i], dp[i-w] + v)
    dp = ndp
print(max(dp))
