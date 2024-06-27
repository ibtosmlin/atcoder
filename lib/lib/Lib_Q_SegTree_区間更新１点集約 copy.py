#title#
# セグメント木双対：区間＜更新・加算・min＞・一点集約
#subtitle#
# 区間更新・一点集約
# 区間加算・一点集約
# 区間min・一点集約

#name#
# 双対セグメント木区間x一点
#description#
# 双対セグメント木区間x一点
#body#

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


###################################################
n, q = map(int, input().split())
INF = float('inf')#(1<<31) - 1
# RUQ = SegmentTree(lambda x, y: max(x, y), INF, n, [INF]*n)
# RAQ = SegmentTree(lambda x, y: (max(x[0], y[0]), x[1]+y[1]), 0, n, [0]*n)
RMinQ = DualSegmentTree(lambda x, y: (max(x[0], y[0]), min(x[1],y[1])), INF, n, [INF]*n)
RMaxQ = DualSegmentTree(lambda x, y: (max(x[0], y[0]), max(x[1],y[1])), INF, n, [INF]*n)

for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, x = qry
        # l -= 1
        r += 1
        RMinQ.update(l, r, x)
    # else:
    #     i = qry[0]
        # i -= 1
        # print(RUQ[i])
        print([RMinQ[i] for i in range(n)])

#prefix#
# Lib_Q_SegDual_双対_区間更新一点集約
#end#
