# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fo
from collections import deque
f = deque([])
s = deque([])
lf = 0
ls = 0
q = int(input())
for _ in range(q):
    que = input().split()
    if que[0] == 'A':
        s.append(que[1])
        ls += 1
    if que[0] == 'B':
        s.appendleft(que[1])
        ls += 1
    if que[0] == 'C':
        f.popleft()
        lf -= 1
    if que[0] == 'D':
        print(f[0])
    if lf < ls:
        x = s.popleft()
        ls -= 1
        f.append(x)
        lf += 1
