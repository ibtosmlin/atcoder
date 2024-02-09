# https://atcoder.jp/contests/abc338/tasks/abc338_b
from collections import Counter
cnt = Counter(input())
maxchar = None
maxcnt = 0
for i in range(26):
    u = chr(i+ord('a'))
    if cnt[u] > maxcnt:
        maxchar = u
        maxcnt = cnt[u]
print(maxchar)
