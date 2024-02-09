# https://atcoder.jp/contests/abc339/tasks/abc339_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
from atcoder.segtree import SegTree

N, D = map(int, input().split())
sgt = SegTree(max, 0, 500010)
for ai in map(int, input().split()):
    l = max(0, ai - D)
    r = min(500000, ai + D) + 1
    v = sgt.prod(l, r) + 1
    sgt.set(ai, v)
print(sgt.all_prod())
