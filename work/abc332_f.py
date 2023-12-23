# https://atcoder.jp/contests/abc332/tasks/abc332_f
import sys; input: lambda _: sys.stdin.readline().rstrip()

from atcoder.lazysegtree import LazySegTree
class LazySegmentTree(LazySegTree):
    # def __init__(self, op, e, mapping, composition, id, v):
    #     super().__init__(op, e, mapping, composition, id, v)

    def __str__(self) -> str:
        return ' '.join(map(str, [self.get(i) for i in range(self._n)]))

    # https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    # set(p, x): p番目の要素をxに置き換える
    # get(p, x): p番目の要素を取得する
    # prod(l, r): 半開区間[l, r)の計算結果を取得する
    # all_prod(): 全区間[0, self._n)計算結果を取得する
    # apply(l, r, f): 半開区間[l, r)の各要素にfを施す
    # max_right(l, g): g(v[i])がTrueとなる一番右のindex（lからスタート）
    # min_left(r, g): g(v[i])がTrueとなる一番左のindex（rからスタート）

#######################################################
mod = 998244353
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    return (x+y) % mod

# op演算の単位元
ie = 0

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f, x):
    a, b = f
    return (a*x + b) % mod

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    a, b = f
    c, d = g
    return (a * c % mod, (a * d + b) % mod)

# 遅延評価演算の単位元
id = (1, 0)

sgt = LazySegmentTree(op, ie, mapping, composition, id, A)

for _ in range(M):
    l, r, x = map(int, input().split())
    l -= 1
    d = r-l
    invd = pow(d, -1, mod)
    a = (d-1) * invd % mod
    b = invd * x % mod
    sgt.apply(l, r, (a, b))

print(sgt)