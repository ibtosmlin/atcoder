#title#
# 遅延評価セグメント木plain
#subtitle#
# 遅延評価セグメント木plain
# LazySegTree:(op, e, mapping, composition, id_, v)

#name#
# 遅延評価セグメント木plain
#description#
# 遅延評価セグメント木

#body#
from atcoder.lazysegtree import LazySegTree
class LazySegmentTree(LazySegTree):
    def __init__(self, op, e, mapping, composition, id, v):
        super().__init__(op, e, mapping, composition, id, v)

    def __str__(self) -> str:
        return ' '.join(map(str, [self.get(i) for i in range(self._n)]))

    def _debug(self, xs):
        strs = [str(x) for x in xs] + [f"({x})" for x in range(self._n)]
        minsize = max(len(s) for s in strs[self._size:])
        result = ["|"] * (self._log + 2)
        level = 0
        next_level = 2
        for i in range(1, len(strs)):
            if i == next_level:
                level += 1
                next_level <<= 1
            if level < self._log + 1:
                width = ((minsize + 1) << (self._log - level)) - 1
            result[level] += strs[i].center(width) + "|"
        return "\n".join(result)


    # https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    # set(p, x): p番目の要素をxに置き換える
    # get(p, x): p番目の要素を取得する
    # prod(l, r): 半開区間[l, r)の計算結果を取得する
    # all_prod(): 全区間[0, self._n)計算結果を取得する
    # apply(l, r, f): 半開区間[l, r)の各要素にfを施す
    # max_right(l, isok): g(v[i])がTrueとなる一番右のindex（lからスタート）
    # min_left(r, isok): g(v[i])がTrueとなる一番左のindex（rからスタート）

#######################################################
n, d = map(int, input().split())
A = list(input().split())
bs = pow(10, d-1)
for i in range(n):
    x = [int(A[i])]
    for j in range(d-1):
        f, s = divmod(x[-1], bs)
        x.append(s*10+f)
    A[i] = x

# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    ret = [0] * d
    for i in range(d):
        ret[i] = x[i]^y[i]
    return ret

# op演算の単位元
ie = [0] * d

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f,x):
    ret = [0] * d
    for i in range(d):
        ret[(i-f)%d] = x[i]
    return ret

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    return (f+g)%d

# 遅延評価演算の単位元
id = 0

sgt = LazySegTree(op, ie, mapping, composition, id, A)


#prefix#
# Lib_Q_LazySeg_plain
#end#
