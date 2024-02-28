# https://atcoder.jp/contests/abc341/tasks/abc341_e
import sys
input = lambda: sys.stdin.readline().rstrip()

from atcoder.lazysegtree import LazySegTree

#######################################################
# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    return (x[0]+y[0], x[1]+y[1])

# op演算の単位元 (区間内の不整合な状態数, 区間内の整合な状態数)
# 不整合とは10101010と一致しないことを言う

ie = (0, 0)

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f,x):
    if f==0: return x
    return (x[1], x[0])

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    return (f+g)%2

# 遅延評価演算の単位元
id = 0

n, q = map(int, input().split())
s = input()
s = [(int(s[i])^(i%2), 1-int(s[i])^(i%2)) for i in range(n)]

sgt = LazySegTree(op, ie, mapping, composition, id, s)
for _ in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    if t == 1:
        sgt.apply(l, r, 1)
    else:
        cnt = sgt.prod(l, r)[0]
        ret = cnt == 0 or cnt == r - l
        print('Yes' if ret else 'No')
