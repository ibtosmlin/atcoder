# https://judge.yosupo.jp/problem/range_affine_point_get
import sys; input: lambda _: sys.stdin.readline().rstrip()

class DualSegmentTree:
    def __init__(self, op, e, v):
        self._op = op
        self._ie = e
        if isinstance(v, int): v = [e] * v
        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._lazy = [e] * (2*self._size)
        self._lazy[self._size:self._size+self._n] = v[:]

    def _propagate_at(self, i):
        self._lazy[i << 1] = self._op(self._lazy[i << 1], self._lazy[i])
        self._lazy[i << 1 | 1] = self._op(self._lazy[i << 1 | 1], self._lazy[i])
        self._lazy[i] = self._ie

    def _propagate_above(self, i):
        for h in range(i.bit_length() - 1, 0, -1):
            self._propagate_at(i >> h)

    def get(self, i):
        i += self._size
        self._propagate_above(i)
        return self._lazy[i]

    def set(self, i: int, a):
        i += self._size
        self._propagate_above(i)
        self._lazy[i] = a

    def apply(self, l, r, g):
        assert 0 <= l and l <= r and r <= self._n
        l += self._size
        r += self._size
        self._propagate_above(l // (l & -l))
        self._propagate_above(r // (r & -r) - 1)
        while l < r:
            if l & 1:
                self._lazy[l] = self._op(self._lazy[l], g)
                l += 1
            if r & 1:
                r -= 1
                self._lazy[r] = self._op(self._lazy[r], g)
            l >>= 1
            r >>= 1

class RangeAffinePointGet(DualSegmentTree):
    def __init__(self, A):
        self.mod = 998244353
        self.bit = 30
        self.msk = (1<<self.bit)-1
        id = 1<<self.bit
        super().__init__(self._op, id, len(A))
        self.A = A

    def _op(self, x, y):
        mod, bit, msk = self.mod, self.bit, self.msk
        a, b = x>>bit, x&msk
        c, d = y>>bit, y&msk
        r0 = (a*c)%mod
        r1 = (b*c+d)%mod
        return r0<<bit|r1

    def apply(self, l, r, u):
        a, b = u
        super().apply(l, r, a<<self.bit|b)

    def get(self, i):
        mod, bit, msk = self.mod, self.bit, self.msk
        u = super().get(i)
        a, b = u>>bit, u&msk
        return (a*self.A[i]+b)%mod

####################################
N, Q = map(int, input().split())
A = list(map(int, input().split()))
sgt = RangeAffinePointGet(A)

for _ in range(Q):
    f, *que = map(int, input().split())
    if f == 0:
        l, r, b, c = que
        sgt.apply(l, r, (b, c))
    else:
        i = que[0]
        print(sgt.get(i))
