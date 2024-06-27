# https://judge.yosupo.jp/problem/point_set_range_composite
import sys; input: lambda _: sys.stdin.readline().rstrip()

class SegmentTree:
    def __init__(self, op, e, v):
        self._f = op
        self._ie = e
        if isinstance(v, int): v = [e] * v
        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._dat = [e] * (2*self._size)
        self._dat[self._size:self._size+self._n] = v
        for i in range(self._size-1, 0, -1):
            self._update(i)

    def _update(self, i):
        self._dat[i] = self._f(self._dat[i*2], self._dat[i*2+1])

    def __getitem__(self, i):
        return self._dat[i + self._size]

    def set(self, p, x):
        p += self._size
        self._dat[i] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def add(self, p, x):
        p += self._size
        self._dat[i] += x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def all_prod(self):
        return self._dat[1]

    def prod(self, l, r):
        l += self._size
        r += self._size
        lret, rret = self._ie, self._ie
        while l < r:    # lとrが重なるまで上記の判定を用いて演算を実行
            if l & 1:
                lret = self._f(lret, self._dat[l])
                l += 1
            if r & 1:
                r -= 1
                rret = self._f(self._dat[r], rret)
            l >>= 1
            r >>= 1
        return self._f(lret, rret)

    def max_right(self, l, isOk):
        if l >= self._n: return self._n
        l += self._size
        sm = self._ie
        while True:
            while l % 2 == 0: l >>= 1
            if not isOk(self._f(sm, self._dat[l])):
                while l < self._size:
                    l <<= 1
                    if isOk(self._f(sm, self._dat[l])):
                        sm = self._f(sm, self._dat[l])
                        l += 1
                return l - self._size
            sm = self._f(sm, self._dat[l])
            l += 1
            if l & -l == l: break
        return self._n

    def min_left(self, r, isOk):
        if r <= 0: return 0
        r += self._size
        sm = self._ie
        while True:
            r -= 1
            while r > 1 and r % 2 == 1: r >>= 1
            if not isOk(self._f(self._dat[r], sm)):
                while r < self._size:
                    r = r << 1 | 1
                    if isOk(self._f(self._dat[r], sm)):
                        sm = self._f(self._dat[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._f(self._dat[r], sm)
            if r & -r == r: break
        return 0


class PointSetRangeComposite(SegmentTree):
    def __init__(self, v):
        self.mod = 998244353
        self.bit = 30
        self.msk = (1<<self.bit)-1
        _v = [a<<self.bit|b for a, b in v]
        super().__init__(_v, self._op, 1<<self.bit)

    def _op(self, x, y):
        mod, bit, msk = self.mod, self.bit, self.msk
        a, b = x>>bit, x&msk
        c, d = y>>bit, y&msk
        r0 = (a*c)%mod
        r1 = (b*c+d)%mod
        return r0<<bit|r1

    def update(self, i, u):
        a, b = u
        super().update(i, a<<self.bit|b)

    def query(self, l, r):
        mod, bit, msk = self.mod, self.bit, self.msk
        u = super().query(l, r)
        a, b = u>>bit, u&msk
        return (a, b)

    def get(self, l, r, x):
        mod, bit, msk = self.mod, self.bit, self.msk
        a, b = self.query(l, r)
        return (a*x+b)%mod

####################################
N, Q = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]
sgt = PointSetRangeComposite(A)

for _ in range(Q):
    f, *que = map(int, input().split())
    if f == 0:
        p, a, b = que
        sgt.update(p, (a, b))
    else:
        l, r, x = que
        print(sgt.get(l, r, x))
