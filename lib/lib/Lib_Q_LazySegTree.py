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
from atcoder.lazysegtree import LazySegTree as LazySegTreeACL

class LazySegTreeMine:
    def __init__(self, op, e, mapping, composition, id_, v):
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
        if isinstance(v, int): v = [e] * v
        self._n = len(v)
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [id_] * 2 * self._size
        for i in range(n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)
    def _update(self, i):
        self._d[i] = self._op(self._d[2 * i], self._d[2 * i + 1])
    def _gindex(self, l, r):
        l += self._size
        r += self._size
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            l >>= 1; r >>= 1
        while l:
            yield l
            l >>= 1
    def _propagates(self, *ids):
        for i in reversed(ids):
            f = self._lz[i]
            self._lz[i] = self._id
            self._lz[2 * i] = self._composition(f, self._lz[2 * i])
            self._lz[2 * i + 1] = self._composition(f, self._lz[2 * i + 1])
            self._d[2 * i] = self._mapping(f, self._d[2 * i])
            self._d[2 * i + 1] = self._mapping(f, self._d[2 * i + 1])
    def apply(self, l, r, f):
        *ids, = self._gindex(l, r)
        self._propagates(*ids)
        l += self._size; r += self._size
        while l < r:
            if l & 1:
                self._lz[l] = self._composition(f, self._lz[l])
                self._d[l] = self._mapping(f, self._d[l])
                l += 1
            if r & 1:
                self._lz[r - 1] = self._composition(f, self._lz[r - 1])
                self._d[r - 1] = self._mapping(f, self._d[r - 1])
            l >>= 1; r >>= 1
        for i in ids:
            self._update(i)
    def prod(self, l, r):
        self._propagates(*self._gindex(l, r))
        resl = self._e
        resr = self._e
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                resl = self._op(resl, self._d[l])
                l += 1
            if r & 1:
                resr = self._op(self._d[r - 1], resr)
            l >>= 1; r >>= 1
        return self._op(resl, resr)
    def get(self, p):
        return self.prod(p, p+1)


class LazySegmentTree(LazySegTreeMine):
#class LazySegmentTree(LazySegTreeACL):
    def __init__(self, op, e, mapping, composition, id_, v):
        super().__init__(op, e, mapping, composition, id_, v)

    def __str__(self) -> str:
        return ' '.join(map(str, [self.get(i) for i in range(self._n)]))

    def _debug(self, xs):
        strs = [str(x) for x in xs] + [f'({x})' for x in range(self._n)]
        minsize = max(len(s) for s in strs[self._size:])
        result = ['|'] * (self._log + 2)
        level = 0
        next_level = 2
        for i in range(1, len(strs)):
            if i == next_level:
                level += 1
                next_level <<= 1
            if level < self._log + 1:
                width = ((minsize + 1) << (self._log - level)) - 1
            result[level] += strs[i].center(width) + '|'
        return '\n'.join(result)


    # https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    # set(p, x): p番目の要素をxに置き換える
    # get(p, x): p番目の要素を取得する
    # prod(l, r): 半開区間[l, r)の計算結果を取得する
    # all_prod(): 全区間[0, self._n)計算結果を取得する
    # apply(l, r, f): 半開区間[l, r)の各要素にfを施す
    # max_right(l, isok): g(v[i])がTrueとなる一番右のindex（lからスタート）
    # min_left(r, isok): g(v[i])がTrueとなる一番左のindex（rからスタート）
#######################################################

# INF = 10 ** 18
# RMinQ and RAQ
# LST = LazySegmentTree([0]*N, min, INF, lambda f, x: f+x, lambda f, g: f+g, 0)
# RMaxQ and RAQ
# LST = LazySegmentTree([0]*N, max, -INF, lambda f, x: f+x, lambda f, g: f+g, 0)
# #RSumQ and RAQ
# op = lambda x, y: (x[0]+y[0], x[1]+y[1])
# mp = lambda f, x: (x[0]+f*x[1], x[1])
# LST = LazySegmentTree([(0,1)]*N, op, (0,0), mp, lambda f, g: f+g, 0)
# #RMinQ and RUQ
# LST = LazySegmentTree([INF]*N, min, INF, lambda f, x: x if f == INF else f, lambda f, g: g if f == INF else f, INF)
# #RMaxQ and RUQ
# LST = LazySegmentTree([-INF]*N, max, -INF, lambda f, x: x if f == -INF else f, lambda f, g: g if f == -INF else f, -INF)
# #RSumQ and RUQ
# op = lambda x, y: (x[0]+y[0], x[1]+y[1])
# mp = lambda f, x: x if f == INF else (f*x[1], x[1])
# LST = LazySegmentTree([(0,1)]*N, op, (0,0), mp, lambda f, g: g if f == INF else f, INF)

# https://github.com/ibtosmlin/atcoder/blob/main/lib/lib/Memo_%E9%81%85%E5%BB%B6%E8%A9%95%E4%BE%A1Seg%E6%9C%A8.md
#######################################################
# 区間集約演算 *: G * G -> G の定義.
def op(x, y):
    invx, c0x, c1x = x
    invy, c0y, c1y = y
    return (invx+invy+c0y*c1x, c0x+c0y, c1x+c1y)

# op演算の単位元(反転数,区間内の０の数,区間内の１の数)
e = (0, 0, 0)

# 区間更新演算 ·: F · G -> G の定義.
def mapping(f, x):
    if f==0: return x
    inv, c0, c1 = x
    return (c1*c0 - inv, c1, c0)

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    return f ^ g

# 遅延評価演算の単位元
id = 0

n, q = map(int, input().split())
a = []
for i in map(int, input().split()):
    if i == 1:
        a.append((0, 0, 1))
    else:
        a.append((0, 1, 0))
sgt = LazySegmentTree(op, e, mapping, composition, id, a)


#prefix#
# Lib_Q_LazySeg_plain
#end#
