#name#
# セグメント木
#description#
# セグメント木
#body#
class SegmentTree:
    """RAQ Segment Tree
    区間加算・1点抽出
    Parameters
    ----------
    a : list
        初期リスト
    e : 単位元
        by default float('inf')
    Notes
    -----
    1-indexed
    https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_E
    """
    def __init__(self, n: int, ie):
        self._n = n                             # 元のデータサイズ
        self._log = (self._n - 1).bit_length()  # seg木の深さ
        self._size = 1 << self._log             # seg木のサイズ
        self.INF = ie
        # seg木の初期化
        self._dat = [self.INF] * (2 * self._size)


    def add(self, l: int, r: int, x: int) -> None:
        """半開区間[l, r)にxを加算
        """
        l += self._size  # 1番下の層におけるインデックス
        r += self._size  # 1番下の層におけるインデックス
        # 左側の答えと右側の答えを初期化
        while l < r:    # lとrが重なるまで上記の判定を用いて演算を実行
            # 右が子同士の右側(rが奇数)(rの末桁=1)ならば、dat[r-1]を演算
            if r & 1:
                r -= 1
                self._dat[r] += x
            # 左が子同士の右側(lが奇数)(lの末桁=1)ならば、dat[l]を演算
            if l & 1:
                self._dat[l] += x
                l += 1
            l >>= 1
            r >>= 1


    def query(self, k: int) -> int:
        """a_kを取得
        """
        k += self._size
        t = 0
        while k > 0:
            if self._dat[k]:
                t += self._dat[k]
            k >>= 1
        return t


    def __getitem__(self, i:int) -> int:
        """index = i の値を求める
        queryと同じ
        """
        return self.query(i)


###################################################
n, q = map(int, input().split())

raq = SegmentTree(n+2, 0)

for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, x = qry
#        l -= 1
        r += 1
        raq.add(l, r, x)
    else:
        i = qry[0]
#        i -= 1
        print(raq[i])

#prefix#
# Lib_Q_seg木（区間加算・一点集約)
#end#
