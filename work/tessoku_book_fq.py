# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fq
from heapq import heapify, heappop, heappush
n, l, k = map(int, input().split())

gs = []
heapify(gs)

now = k
ret = 0
last = 0
for _ in range(n):
    a, c = map(int, input().split())
    if now >= a:
        now -= a
        heappush(gs, (c, a, k - (now-a)))
        # c, a, nokori
    else:
        while gs and now < a:
            c, a, r = heappop(gs)
