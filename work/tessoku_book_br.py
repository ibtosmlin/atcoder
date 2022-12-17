# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_br
import sys
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
INF = 10**9
n, m = map(int, input().split())
a = 0
for i, v in enumerate(list(map(int, input().split()))):
    if v: a += 1<<i

dp = [INF] * (1<<n)
dp[a] = 0
for _ in range(m):
    x, y, z = map(int1, input().split())
    ndp = [INF] * (1<<n)
    xyz = (1<<x) + (1<<y) + (1<<z)
    for i in range(1<<n):
        if dp[i] == INF: continue
        ndp[i] = min(ndp[i], dp[i])
        ndp[i^xyz] = min(ndp[i^xyz], dp[i] + 1)
    dp = ndp
ret = dp[-1]
print(-1 if ret == INF else ret)