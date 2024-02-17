# https://atcoder.jp/contests/abc341/tasks/abc341_e
import sys
input = lambda: sys.stdin.readline().rstrip()

from atcoder.segtree import SegTree

n, q = map(int, input().split())
s = list(input())
sgt = SegTree(lambda x, y: x + y, 0, [0]*n)
for i in range(n-1):
    if s[i] == s[i+1]: sgt.set(i, 1)

for _ in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    if t == 1:
        if l > 0:
            sgt.set(l-1, 1-sgt.get(l-1))
        if r < n:
            sgt.set(r-1, 1-sgt.get(r-1))
    else:
        ret = sgt.prod(l, r-1) == 0
        print('Yes' if ret else 'No')
