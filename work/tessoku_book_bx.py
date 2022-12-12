# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bx
from bisect import bisect_left, bisect_right
mod = 10**9 + 7
n, w, l, r = map(int, input().split())
x = [0] + list(map(int, input().split())) + [w]
N = len(x)
dp = [0] * N
dp[0] = 1


for i in range(1, N):
    xi = x[i]
    rp = bisect_right(x, xi - l) - 1
    lp = bisect_left(x, xi - r)
#    print(lp, rp,xi, xi-r, xi-l)
    dp[i] = rdp[rp] - rdp[lp]
    dp[i] %= mod
    rdp.append((rdp[-1]+dp[i])%mod)

print(dp[-1])
