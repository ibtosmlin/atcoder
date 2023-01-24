# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fn
from heapq import heapify, heappop, heappush

n, m, k = map(int, input().split())
# dp[i]: 今iにいて飛行機に乗れる人の最大飛行回数
dp = [0] * ((n+1) *2 )

events = []
heapify(events)
for _ in range(m):
    a, s, b, t = map(int, input().split())
    heappush(events, (s, t, a, b, 0))

while events:
    s, t, fm, to, count = heappop(events)
    if fm < n:  #hikoukinoru
        dp[b+n] = max(dp[b+n], count + 1)
        heappush(events, (t, t+k, b+n, b, count))
    else:
        heappush(events, (t, t+k, )
        dp[a] = max(dp[a], b)
    print(dp)
print(max(dp))