
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


####################################

n, q = map(int, input().split())

def op(x, y):
    return x

sgt = DualSegmentTree(op, -1, [(1 << 31)-1] * n)
for _ in range(q):
    t, *que = map(int, input().split())
    if t == 0:
        l, r, b = que
        sgt.apply(l, r+1, b)
    else:
        i, = que
        v = sgt.get(i)
        print(v)
