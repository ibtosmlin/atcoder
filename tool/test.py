#title#
# セグメント木区間更新・一点集約
#subtitle#
# 区間更新・一点集約
# 区間加算・一点集約

#name#
# セグメント木区間x一点
#description#
# セグメント木区間x一点
#body#
class SegmentTree:  # 初期化処理
    """cheap Segment Tree
    区間更新・1点抽出
    Parameters
    ----------
    op: monoid
    ie: 単位元
    n : list
    A : 初期リスト
    Notes
    -----
    1-indexed
    https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_D
    https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_E
    """
    def __init__(self, op, ie, n, A=None):
        self._n = n                             # 元のデータサイズ
        self._log = (self._n - 1).bit_length()  # seg木の深さ
        self._size = 1 << self._log             # seg木のサイズ
        self._counter = 0
        self.INF = (-1, ie)
        # seg木の初期化
        self._dat = [self.INF] * (2 * self._size)
        self._op = op
        if A:
            for i, ai in enumerate(A):
                self.update(i, i+1, ai)


    def update(self, l, r, x):
        """半開区間[l, r)の値を更新
        """
        _x = (self._counter, x)
        l += self._size
        r += self._size
        while l < r:
            if r & 1:
                r -= 1; self._dat[r] = self._op(self._dat[r], _x)
            if l & 1:
                self._dat[l] = self._op(self._dat[l], _x); l += 1
            l >>= 1; r >>= 1
        self._counter += 1

    def _query(self, k):
        k += self._size
        t = self.INF
        while k > 0:
            if self._dat[k]:
                t = self._op(t, self._dat[k])
            k >>= 1
        return t

    def query(self, k: int) -> int:
        """a_kを取得
        """
        return self._query(k)[1]

    def __getitem__(self, i:int) -> int:
        return self.query(i)


###################################################
n, q = map(int, input().split())
INF = (1<<31) - 1
RUQ = SegmentTree(lambda x, y: max(x, y), INF, n, [INF]*n)
RAQ = SegmentTree(lambda x, y: (max(x[0], y[0]), x[1]+y[1]), 0, n, [0]*n)

for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, x = qry
        # l -= 1
        r += 1
        RUQ.update(l, r, x)
    else:
        i = qry[0]
        # i -= 1
        print(RUQ[i])

#prefix#
# Lib_Q_Seg_区間更新一点集約
#end#