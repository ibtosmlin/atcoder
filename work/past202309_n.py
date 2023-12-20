# https://atcoder.jp/contests/past16-open/tasks/past202309_n

class SegmentTree:  # 初期化処理
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


####################################
from collections import defaultdict

Q, K = map(int, input().split())
mod = 998244353
ie = (0, 0)
def op(x, y):
    a, b = x
    c, d = y
    return ((a+c*pow(K, b, mod))%mod, b+d)
query = []
values = set()
cnt = defaultdict(int)

for i in range(Q):
    f, x = input().split()
    f = f == "+"
    x = int(x)
    if f:
        cnt[x] += 1
        query.append((f, x, cnt[x]))
        values.add((x, cnt[x]))
    else:
        query.append((f, x, cnt[x]))
        cnt[x] -= 1

vs = {v:i for i, v in enumerate(sorted(values))}
sgt = SegmentTree(Q, op, ie)
for f, x, c in query:
    if f:
        sgt.update(vs[(x, c)], (x, 1))
    else:
        sgt.update(vs[(x, c)], (0, 0))
    print(sgt.query(0, Q)[0])
