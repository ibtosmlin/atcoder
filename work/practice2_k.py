# https://atcoder.jp/contests/practice2/tasks/practice2_k
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
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
n, q = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    return (x+y)% mod

# op演算の単位元
ie = 0

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f,x):
    return (f[0] * x + f[1]) % mod

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    # f・g = a * (c*x+d) + b
    # f・g = a*c * x + a*d+b
    return (f[0] * g[0] % mod, (f[0]*g[1] + f[1])%mod)

# 遅延評価演算の単位元
id = (1, 0)

sgt = LazySegmentTree(op, ie, mapping, composition, id, A)
for _ in range(q):
    f, *que = map(int, input().split())
    if f == 0:
        l, r, b, c = que
        sgt.apply(l, r, (b, c))
    else:
        l, r = que
        print(sgt.prod(l, r))

print(sgt)