#name#
# セグメント木１点更新区間集約
#description#
# セグメント木１点更新区間集約
#body#
class SegmentTree:  # 初期化処理
    """Segment Tree
    一点更新・区間集約
    Parameters
    ----------
    init : list
        初期リスト
    f : SegmentTreeにのせるモノイド
        作用素
    ie : fに対する単位元
    Notes
    -----
    1-indexed
    https://atcoder.jp/contests/practice2/tasks/practice2_j
    モノイドとは、集合と二項演算の組で、結合法則と単位元の存在するもの
    ex. +, max, min
    [ 1] a0 ・ a1  ・ a2 ・ a3 ・ a4 ・ a5 ・ a6 ・ a7  ->[0]
    [ 2] a0 ・ a1  ・ a2 ・ a3       [ 3] a4 ・ a5 ・ a6・ a7
    [ 4] a0 ・ a1    [ 5] a2 ・ a3   [ 6] a4 ・ a5   [ 7] a6 ・ a7
    [ 8] a0 [ 9] a1  [10] a2 [11] a3 [12] a4 [13] a5 [14] a6 [15] a7
                          [0001]
              [0010]                  [0011]
        [0100]      [0101]      [0110]      [0111]
     [1000][1001][1010][1011][1100][1101][1110][1111]
    size = 8  元の配列数の２べき乗値
    親のインデックス         i//2 or i>>=1 bitで一個右シフト
    左側の子のインデックス    2*i
    右側の子のインデックス    2*i+1
    aiの値が代入されているインデックス    i+size
    """
    def __init__(self, init, f, ie):
        self._f = f
        self._ie = ie
        if type(init) == int:
            init = [ie] * init
        self._n = len(init)
        self._log = (self._n - 1).bit_length()  # seg木の深さ
        self._size = 1 << self._log     # seg木のサイズ
        # seg木の初期化
        self._dat = [ie] * self._size + init + [ie] * (self._size - len(init))
        for i in range(self._size-1, 0, -1):
            self._update(i)


    def _update(self, i):
        # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
        self._dat[i] = self._f(self._dat[i*2], self._dat[i*2+1])


    def __getitem__(self, i):
        """index = i の値を求める
        """
        return self._dat[i + self._size]


    def __str__(self):
        """元のリストの値を表示
        """
        return ' '.join(map(str, (self[i] for i in range(self._n))))


    def update(self, i, x):
        """one point update
        a[i] を xに更新
        """
        #
        i += self._size
        self._dat[i] = x
        while i > 0:    # 層をのぼりながら値を更新 indexが0になれば終了
            i >>= 1     # 1つ上の層のインデックス(完全二分木における親)
            # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
            self._update(i)


    def add(self, i, x):
        """one point update
        a[i] に xを加算
        """
        #
        i += self._size
        self._dat[i] += x
        while i > 0:    # 層をのぼりながら値を更新 indexが0になれば終了
            i >>= 1     # 1つ上の層のインデックス(完全二分木における親)
            # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
            self._update(i)


    def query(self, l, r):
        """半開区間[l, r)にf(a[l], a[l+1])演算
        """
        # モノイドでは可換律は保証されていないので演算の方向に注意
        l += self._size  # 1番下の層におけるインデックス
        r += self._size  # 1番下の層におけるインデックス
        # 左側の答えと右側の答えを初期化
        lret, rret = self._ie, self._ie
        while l < r:    # lとrが重なるまで上記の判定を用いて演算を実行
            # 左が子同士の右側(lが奇数)(lの末桁=1)ならば、dat[l]を演算
            if l & 1:
                lret = self._f(lret, self._dat[l])
                l += 1
            # 右が子同士の右側(rが奇数)(rの末桁=1)ならば、dat[r-1]を演算
            if r & 1:
                r -= 1
                rret = self._f(self._dat[r], rret)
            l >>= 1
            r >>= 1
        return self._f(lret, rret)


    def max_right(self, l, isOk):
        """
        ex:
        maxの場合 a[l]  a[r-1] が isOKとなる最大の値
        (1): 関数 bool isOk(x) を定義し、segtreeの上で二分探索をする。
        (2): 木の値を引数にとりboolを返す関数オブジェクトを渡して使用します。
        r = l もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
        r = n もしくは f(op(a[l], a[l + 1], ..., a[r])) = false
        fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最大のr
        """
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
        """
        l = r もしくは f(op(a[l], a[l + 1], ..., a[r - 1])) = true
        l = 0 もしくは f(op(a[l-1], a[l], ..., a[r-1])) = false
        fが単調だとすれば、f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最小のl
        """
        if r <= 0: return 0
        r += self._size
        sm = self._ie
        while True:
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


####################################
class RMaxQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, max, -float('inf'))

class RMinimumQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, min, float('inf'))

class RSumQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, lambda x, y: x + y, 0)

class RProdQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, lambda x, y: x * y, 1)

class RXorQSegmentTree(SegmentTree):
    def __init__(self, init):
        super().__init__(init, lambda x, y: x ^ y, 0)

# GCD query
from math import gcd
ie = float('inf')
def op(x, y):
    if x == ie: return y
    if y == ie: return x
    return gcd(x, y)

sgt = SegmentTree(a, op, ie)

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
