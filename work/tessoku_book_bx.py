# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bx
import bisect
mod = 10**9+7
n, w, l, r = map(int, input().split())
x = [0] + list(map(int, input().split())) + [w]
n += 2
dp = [0] * n
dp[0] = 1
rdp = [0] * (n+1)
rdp[1] = 1

for i in range(1, n):
    xi = x[i]
    li = bisect.bisect_left(x, xi - r)
    ri = bisect.bisect_right(x, xi - l)
    dp[i] = rdp[ri] - rdp[li]
    dp[i] %= mod
    rdp[i+1] = rdp[i] + dp[i]
    rdp[i+1] %= mod

print(dp[-1])
#print(dp)
#print(rdp)