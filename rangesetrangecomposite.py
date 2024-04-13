class LazySegTreeLight:
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


class LazySegmentTree(LazySegTreeLight):
    def __init__(self, op, e, mapping, composition, id, v):
        super().__init__(op, e, mapping, composition, id, v)

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



#######################################################
mod = 998244353
bit = 30
msk = (1<<bita) - 1

n, q = map(int, input().split())
A = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append((a<<bita|b)<<bitb|1)
# 区間集約演算 *: G * G -> G の定義.

def op(x, y):
    xa, xb, xlen = x>>(bita+bitb), (x>>bitb)&mskb, x&mskc
    ya, yb, ylen = y>>(bita+bitb), (y>>bitb)&mskb, y&mskc
    return (((xa*ya%mod)<<bita)|(xb*ya+yb)%mod)<<bitb|(xlen+ylen)

# op演算の単位元
ie = 1<<(bita+bitb)

# 区間更新演算 ·: F · G -> G の定義.
def _fast_pow(a: int, b: int) -> int:
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def mapping(f,x):
    if f==id: return x
    fa, fb, flen = f>>(bita+bitb), (f>>bitb)&mskb, f&mskc
    xa, xb, xlen = x>>(bita+bitb), (x>>bitb)&mskb, x&mskc
    A = _fast_pow(fa, xlen)
    if fa <= 1:
        B = xlen*fa * fb % mod
    else:
        B = (A-1) * _fast_pow(fa-1, mod-2) * fb % mod
    return (A<<bita|B)<<bitb|xlen

# 遅延評価演算 ·: F · F -> F の定義.
def composition(f, g):
    return g if f == id else f

# 遅延評価演算の単位元
id = 1<<bitb - 1

sgt = LazySegmentTree(op, ie, mapping, composition, id, A)
for _ in range(q):
    f, l, r, *v = map(int, input().split())
    if f:
        x = sgt.prod(l, r)
        xa, xb, xlen = x>>(bita+bitb), (x>>bitb)&mskb, x&mskc
        print((xa*v[0]+xb)%mod)
    else:
        sgt.apply(l, r,((v[0]<<bita)|v[1])<<bitb|1)
#prefix#
# Lib_Q_LazySeg_plain
#end#
