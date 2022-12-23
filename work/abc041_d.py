# https://atcoder.jp/contests/abc041/tasks/abc041_d
n, m = map(int, input().split())



dp = [-1] * (1<<n)
for i in range(n):
    dp[1<<i] = 1

for s in range(1, 1<<n):
    for i in range(n):
        if s >> i & 1:
            fm = s^(1 << i)
            if dp[fm] == -1: continue
            isok = True
            for j in range(n):
                if fm >> i & 1:
                    if i in G[j]:
                        isok = False
            if isok:
                dp[s] += dp[fm]

print(dp[-1])