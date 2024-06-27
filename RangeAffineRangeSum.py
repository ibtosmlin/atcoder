# https://judge.yosupo.jp/problem/range_affine_range_sum
import sys; input: lambda _: sys.stdin.readline().rstrip()

class LazySegTreeMine:
    def __init__(self, op, e, mapping, composition, id_, v):
        n = len(v)
        self._n = n
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
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


class RangeAffineRangeSum(LazySegTreeMine):
    def __init__(self, v):
        self.mod = 998244353
        self.bit = 30
        self.msk = (1<<self.bit)-1
        e = 0
        id = 1 << self.bit
        _v = [vi<<self.bit|1 for vi in v]
        super().__init__(self._op, e, self._mapping, self._composition, id, _v)

    def _op(self, x, y):
    # 区間集約演算 *: G * G -> G の定義.
        mod, bit, msk = self.mod, self.bit, self.msk
        xv, xlen = x>>bit, x&msk
        yv, ylen = y>>bit, y&msk
        r0 = (xv+yv)%mod
        r1 = (xlen+ylen)%mod
        return r0<<bit|r1

    # 区間更新演算 ·: F · G -> G の定義.
    def _mapping(self, f,x):
        mod, bit, msk = self.mod, self.bit, self.msk
        f0, f1 = f>>bit, f&msk
        sx, lx = x>>bit, x&msk
        r0 = (f0*sx + f1*lx)%mod
        r1 = lx
        return r0<<bit|r1

    # 遅延評価演算 ·: F · F -> F の定義.
    def _composition(self, f, g):
        mod, bit, msk = self.mod, self.bit, self.msk
        f0, f1 = f>>bit, f&msk
        g0, g1 = g>>bit, g&msk
        r0 = f0*g0%mod
        r1 = (f0*g1+f1)%mod
        return r0<<bit|r1

    def prod(self, l, r):
        u = super().prod(l, r)
        return u >> self.bit

    def apply(self, l, r, u):
        a, b = u
        super().apply(l, r, a<<self.bit|b)

#######################################################


n, q = map(int, input().split())
A = list(map(int, input().split()))

sgt = RangeAffineRangeSum(A)

for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, (a, b) = qry
        sgt.apply(l, r, (a, b))
    else:
        l, r = qry
        print(sgt.prod(l, r))