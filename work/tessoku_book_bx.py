# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bx
from bisect import bisect_left, bisect_right
mod = 10**9 + 7
n, w, l, r = map(int, input().split())
x = [0] + list(map(int, input().split())) + [w]
N = len(x)
dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1

print(x)
for i in range(1, N):
    xi = x[i]
    rp = bisect_right(x, xi - l-1)
    lp = bisect_left(x, xi - r)
#    print(lp, rp,xi, xi-r, xi-l)
    dp[i+1] = dp[rp+1] - dp[lp] + dp[i]
    dp[i+1] %= mod

#    rdp.append((rdp[-1]+dp[i])%mod)
    print(lp, rp, xi-r, xi-l)
print(dp)
