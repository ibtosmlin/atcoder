#name#
# 遅延評価セグメント木code
#description#
# 遅延評価セグメント木
#body#
import sys
def input(): return sys.stdin.readline().rstrip()

####################################
import sys
class LazySegTree:
    def __init__(self, op, e, mapping, composition, id_, v):
        n = len(v)
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
        self._size = 1 << (n - 1).bit_length()
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


INF = (1<<31) - 1


N, Q = map(int, input().split())

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
op = lambda x, y: (x[0]+y[0], x[1]+y[1])
mp = lambda f, x: x if f == INF else (f*x[1], x[1])
LST = LazySegTree([(0,1)]*N, op, (0,0), mp, lambda f, g: g if f == INF else f, INF)


ans = []
for _ in range(Q):
    t, *cmd = map(int, input().split())
    if t:
        s, t = cmd
        ans.append(str(LST.query(s, t+1)[0]))
    else:
        s, t, x = cmd
        LST.apply(s, t+1, x)
print('\n'.join(ans))
#prefix#
# Lib_Q_LazySeg_plain
#end#
