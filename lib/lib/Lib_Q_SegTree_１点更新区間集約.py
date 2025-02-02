#title#
# セグメント木１点更新区間集約
#subtitle#
# SegmentTree(op, e, v):
# op: モノイドの演算
# e: モノイドの単位元
# v: 要素数orリスト

#name#
# セグメント木１点更新区間集約
#description#
# セグメント木１点更新区間集約
#body#

from atcoder.segtree import SegTree

class SegmentTreeMine:
    def __init__(self, op, e, v):
        self._op = op
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
        self._dat[i] = self._op(self._dat[i*2], self._dat[i*2+1])

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
                lret = self._op(lret, self._dat[l])
                l += 1
            if r & 1:
                r -= 1
                rret = self._op(self._dat[r], rret)
            l >>= 1
            r >>= 1
        return self._op(lret, rret)

    def max_right(self, l, isOk):
        if l >= self._n: return self._n
        l += self._size
        sm = self._ie
        while True:
            while l % 2 == 0: l >>= 1
            if not isOk(self._op(sm, self._dat[l])):
                while l < self._size:
                    l <<= 1
                    if isOk(self._op(sm, self._dat[l])):
                        sm = self._op(sm, self._dat[l])
                        l += 1
                return l - self._size
            sm = self._op(sm, self._dat[l])
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
            if not isOk(self._op(self._dat[r], sm)):
                while r < self._size:
                    r = r << 1 | 1
                    if isOk(self._op(self._dat[r], sm)):
                        sm = self._op(self._dat[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._op(self._dat[r], sm)
            if r & -r == r: break
        return 0


class SegmentTree(SegTree):
# class SegmentTree(SegmentTreeMine):
    def __init__(self, op, e, v) -> None:
        super().__init__(op, e, v)

    def __getitem__(self, i):
        """index = i の値を求める"""
        return self._d[i + self._size]

    def __str__(self):
        """元のリストの値を表示"""
        return self._debug(self._d)

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

    def add(self, i, x):
        """one point add a[i] に xを加算 """
        self.set(i, self._d[i + self._size] + x)

    # def max_right(self, l, isOk):
        # ex:
        # maxの場合 a[l]  a[r-1] が isOKとなる最大の値
        # (1): 関数 bool isOk(x) を定義し、segtreeの上で二分探索をする。
        # (2): 木の値を引数にとりboolを返す関数オブジェクトを渡して使用します。
        # r = l もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
        # r = n もしくは f(op(a[l], a[l + 1], ..., a[r])) = false
        # fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最大のr

    # def min_left(self, r, isOk):
    #     l = r もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
    #     l = 0 もしくは f(op(a[l-1], a[l], ..., a[r-1])) = false
    #     fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最小のl

####################################
class RMaxQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(max, -float('inf'), init)

class RMinimumQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(min, float('inf'), init)

class RSumQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(lambda x, y: x + y, 0, init)

class RProdQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(lambda x, y: x * y, 1, init)

class RXorQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(lambda x, y: x ^ y, 0, init)

import math

class RGCDSegmentTree(SegmentTree):
    def __init__(self, init):
        def op(x, y):
            if x == 0: return y
            if y == 0: return x
            return math.gcd(x, y)
        super().__init__(op, 0, init)


####################################
# https://atcoder.jp/contests/practice2/tasks/practice2_j
n, q = map(int, input().split())
A = list(map(int, input().split()))
sgt = RMaxQSegmentTree(A)
for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 1:
        sgt.set(u-1, v)
    elif t == 2:
        print(sgt.prod(u-1, v))
    else:
        print(sgt.max_right(u-1, lambda y: y<v) + 1)

#prefix#
# Lib_Q_Seg_一点更新区間集約
#end#
