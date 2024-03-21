#name#
# 遅延評価セグメント木plain
#description#
# 遅延評価セグメント木
#body#
import sys
def input(): return sys.stdin.readline().rstrip()

####################################
class LazySegmentTree:
    # 初期化処理
    # op  (G, G) -> G : SegmentTreeにのせるモノイド
    # ie : opに対する単位元
    # mapping : (F, G) -> G
    # composition : (F, F) -> F
    # id : compositionに対する単位元

    def __init__(self, init, op, ie, mapping, composition, id):
        self._op = op; self._ie = ie
        if type(init) == int: init = [ie] * init
        self._n = len(init)
        self._log = (self._n-1).bit_length(); self._size = 1 << self._log
        self._dat = [ie] * (2*self._size)
        for i in range(self._n):
            self._dat[self.size+i] = init[i]
        for i in range(self._size-1, 0, -1): self._update(i)
        self._id = id; self._lazy = [id] * self._size
        self._mapping = mapping; self._composition = composition

    def set(self, i, x):    # 一点更新
        i += self._size
        for k in range(self._log, 0, -1): self._push(i >> k)
        self._dat[i] = x
        while i > 0:
            i >>= 1; self._update(i)

    def getvalue(self, i):  # 一点取得
        i += self._size
        for k in range(self._log, 0, -1): self._push(i >> k)
        return self._dat[i]

    def prod(self, l, r):   # range query
        if l == r: return self._ie
        l += self._size; r += self._size
        for i in range(self._log,0,-1):
            if (((l>>i)<<i)!=l):self._push(l>>i)
            if (((r>>i)<<i)!=r):self._push(r>>i)
        lret, rret = self._ie, self._ie  # 左側の答えと右側の答えを初期化
        while l < r:    # lとrが重なるまで上記の判定を用いて演算を実行
            # 左が子同士の右側(lが奇数)(lの末桁=1)ならば、dat[l]を加算
            if l & 1:
                lret = self._op(lret, self._dat[l])
                l += 1
            # 右が子同士の右側(rが奇数)(rの末桁=1)ならば、dat[r-1]を演算
            if r & 1:
                r -= 1
                rret = self._op(self._dat[r], rret)
                # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1; r >>= 1
        return self._op(lret, rret)

    def all_prod(self): return self._dat[1]
    def query(self, l, r): return self.prod(l, r)

    def apply(self, l, r, f):
        if l == r: return
        l += self._size; r += self._size
        for i in range(self._log,0,-1):
            if (((l>>i)<<i)!=l):self._push(l>>i)
            if (((r>>i)<<i)!=r):self._push((r-1)>>i)
        _l, _r = l, r
        while l < r:
            if l & 1:
                self._apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._apply(r, f)
            l >>= 1; r >>= 1
        l, r = _l, _r
        for i in range(1,self._log+1):
            if (((l>>i)<<i)!=l):self._update(l>>i)
            if (((r>>i)<<i)!=r):self._update((r-1)>>i)

    def max_right(self, l, isOk):
        if l >= self._n: return self._n
        l += self._size
        for i in range(self._log, 0, -1): self._push(l >> i)
        sm = self._ie
        while True:
            while l % 2 == 0: l >>= 1
            if not isOk(self._op(sm, self._dat[l])):
                while l < self._size:
                    self._push(l); l <<= 1
                    if isOk(self._op(sm, self._dat[l])):
                        sm = self._op(sm, self._dat[l]); l += 1
                return l - self._size
            sm = self._op(sm, self._dat[l])
            l += 1
            if l & -l == l: break
        return self._n

    def min_left(self, r, isOk):
        if r <= 0: return 0
        r += self._size
        for i in range(self._log, 0, -1): self._push((r - 1) >> i)
        sm = self._ie
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1
            if not isOk(self._op(self._dat[r], sm)):
                while r < self._size:
                    self._push(r); r = r << 1 | 1
                    if isOk(self._op(self._dat[r], sm)):
                        sm = self._op(self._dat[r], sm); r -= 1
                return r + 1 - self._size
            sm = self._op(self._dat[r], sm)
            if r & -r == r: break
        return 0

    def _update(self, i):
        self._dat[i] = self._op(self._dat[i*2], self._dat[i*2+1])
    def _apply(self, i, f):
        self._dat[i] = self._mapping(f, self._dat[i])
        if i < self._size: self._lazy[i] = self._composition(f, self._lazy[i])
    def _push(self, i):
        self._apply(i<<1, self._lazy[i]); self._apply(i<<1|1, self._lazy[i])
        self._lazy[i] = self._id
    def __str__(self) -> str:
        ret = [0] * self._n
        for i in range(self._n): ret[i] = self.getvalue(i)
        return ' '.join(map(str, ret))

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
LST = LazySegmentTree([(0,1)]*N, op, (0,0), mp, lambda f, g: g if f == INF else f, INF)


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
