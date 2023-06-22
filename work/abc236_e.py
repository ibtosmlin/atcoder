# https://atcoder.jp/contests/abc236/tasks/abc236_e
INF = 10**10
n = int(input())
a = list(map(int, input().split()))

def isok1(k):
    dp = [0, 0] * 2
    for i in range(n):
        ndp = [-INF, -INF]
        ndp[1] = max(dp[0], dp[1]) + (a[i] - k)
        ndp[0] = dp[1]
        dp = ndp
    return max(dp) >= 0

def isok2(k):
    dp = [0, 0] * 2
    for i in range(n):
        ndp = [-INF, -INF]
        if a[i] >= k:
            ndp[0] = max(dp[0], dp[1]) + 1
            ndp[1] = dp[0]
        else:
            ndp[0] = max(dp[0], dp[1]) - 1
            ndp[1] = dp[0]
        dp = ndp
    return max(dp) > 0

ok = 0
ng = INF
while ng - ok > 0.00001:
    mid = (ng + ok) / 2
    if isok1(mid):
        ok = mid
    else:
        ng = mid

mean = ok

ok = 0
ng = INF
while ng - ok > 1:
    mid = (ng + ok) // 2
    if isok2(mid):
        ok = mid
    else:
        ng = mid

medi = ok

print(mean)
print(medi)

