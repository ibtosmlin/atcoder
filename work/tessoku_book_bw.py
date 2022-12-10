n = int(input())
dp = [-1] * 1441
dp[0] = 0
q = [list(map(int, input().split())) for _ in range(n)]
q.sort(key=lambda x:x[1])

for _ in range(n):
    t, d = q[_]
    for s in range(1441)[::-1]:
        if dp[s] == -1: continue
        if s+t<=d:
            dp[s+t] = max(dp[s+t], dp[s] + 1)
print(max(dp))