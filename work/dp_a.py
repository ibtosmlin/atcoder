n = int(input())
h = list(map(int, input().split()))
INF = 10**9
dp = [INF] * n
for i in range(n):
    if i == 0:
        dp[i] = 0
    else:
        dp[i] = min(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
        if i - 2 >=0:
            dp[i] = min(dp[i], dp[i-2] + abs(h[i] - h[i-2]))
print(dp[-1])
