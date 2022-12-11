# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bx


n, w, l, r = map(int, input().split())
x = [0] + list(map(int, input().split())) + [w]
dp = [0] * (n+2)
dp[0] = 1
ndp = [0] * (n+3)
ndp[1] = 1

pl, pr = 0, 0

for i, xi in enumerate(x):
    if i == 0: continue
    while pl < i and not (l <= xi - x[pl] <= r):
        pl += 1
    pr = pl
    while pr < i and (l <= xi - x[pr] <= r):
        pr += 1
    dp[i] = ndp[pr] - ndp[pl]
    ndp[i+1] += dp[i] + ndp[i]
    print(pr, pl)
print(dp[-1])
print(dp)
print(ndp)
