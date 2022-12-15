# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bt
h, w, k = map(int, input().split())
c = list(input() for _ in range(h))
d = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if c[i][j] == '#': d[i][j] = 1

ret = 0
for s in range(1<<h):
    now = 0
    other = []
    for i in range(h):
        if s >> i & 1:
            now += 1
    for j in range(w):
        now2 = 0
        for k in range(h):
            if s >> k & 1 == 0:
                now2 += d[k][j]
        other.append(now2)
    other.sort()
    other[:k-]