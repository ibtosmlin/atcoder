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

# op: モノイドの演算
# e: モノイドの単位元
# v: 要素数orリスト

from atcoder.segtree import SegTree

class SegmentTree(SegTree):
    def __init__(self, op, e, v) -> None:
        if isinstance(v, int): v = [e] * v
        super.__init__(self, op, e, v)

    def __getitem__(self, i):
        """index = i の値を求める"""
        return self._dat[i + self._size]

    def __str__(self):
        """元のリストの値を表示"""
        return ' '.join(map(str, (self[i] for i in range(self._n))))

    def update(self, i, x):
        """one point update a[i] を xに更新 """
        self.set(i, x)

    def add(self, i, x):
        """one point add a[i] に xを加算 """
        self.set(i, self._d[i] + x)

    def query(self, l, r):
        """半開区間[l, r)にf(a[l], a[l+1])演算 """
        return self.prod(l, r)

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

# GCD query
from math import gcd
ie = 0
A = [2, 3, 6]
def op(x, y):
    if x == ie: return y
    if y == ie: return x
    return gcd(x, y)

sgt = SegmentTree(op, ie, A)

####################################


# n, q = map(int, input().split())
# a = list(map(int, input().split()))

a = [1,2,3,2,1,3,3,5,2,1]
# sgt = SegmentTree(a, op, ie)
x, v = 3, 55123
l, r = 2, 5
sgt.update(x, v)
print(sgt.query(l, r))
# max_right   lを固定してlambdaを満たす最大のr
# min_left    rを固定してlambdaを満たす最小のl
for l in range(10):
    r = sgt.max_right(l, lambda q: q > 2)
    print(l, r, sgt.query(l, r))

#print(sgt)

#prefix#
# Lib_Q_Seg_一点更新区間集約
#end#
