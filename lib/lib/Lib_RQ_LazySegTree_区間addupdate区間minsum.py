#name#
# 遅延評価セグメント木
#description#
# 遅延評価セグメント木
#body#
import sys
def input(): return sys.stdin.readline().rstrip()

####################################
class LazySegmentTree_RAQ:
    """RAQRangeQuery
    区間加算・区間Min/Sum
    Parameters
    ----------
    a : list
        初期リスト
    e : 単位元
        by default float('inf')
    Attributes
    ----------
    log : int
        木の高さ
    size : int
        木のノード数
    data : list
        木のノードの値
    lazy : list
        遅延評価用値
    """
    def __init__(self, a:list, f, ie, type) -> None:
        self.type = type.lower()
        self.f = f
        self.INF = ie
        self.n = len(a)
        self.log = self.n.bit_length()
        self.size = 1 << self.log
        self.data = [self.INF] * (2*self.size)
        self.lazy = [0] * (2*self.size)
        for i, ai in enumerate(a):
            self.data[i + self.size] = ai
        for i in range(self.size)[::-1]:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])

    def _prop_value(self, v):
        if self.type == 'min':
            return v
        elif self.type == 'sum':
            return v // 2

    def _update_value(self, x):
        if self.type == 'min':
            return x
        elif self.type == 'sum':
            return x * 2

    def __gindex(self, l, r):
        """伝搬される区間のインデックス(1-indexed)を全て列挙するgenerator
        """
        L = l + self.size; R = r + self.size
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1


    def __propagates(self, *ids):
        """遅延伝搬処理
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if not v: continue
            v = self._prop_value(v)
            self.lazy[2*i] += v
            self.lazy[2*i+1] += v
            self.data[2*i] += v
            self.data[2*i+1] += v
            self.lazy[i] = 0


    def update(self, l: int, r: int, x: int) -> None:
        """半開区間[l, r)に対して値xxを加算
        """
        *ids, = self.__gindex(l, r)
        self.__propagates(*ids)
        L = self.size + l; R = self.size + r
        xx = x
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R] += xx
                self.data[R] += xx
            if L & 1:
                self.lazy[L] += xx
                self.data[L] += xx
                L += 1
            L >>= 1; R >>= 1
            xx = self._update_value(xx)
        for i in ids:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])
            self.data[i] += self.lazy[i]


    def query(self, l: int, r: int) -> None:
        """半開区間[l, r)内のfを求める
        """
        self.__propagates(*self.__gindex(l, r))
        L = self.size + l; R = self.size + r

        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = self.f(s, self.data[R])
            if L & 1:
                s = self.f(s, self.data[L])
                L += 1
            L >>= 1; R >>= 1
        return s


    def __getitem__(self, i:int) -> int:
        """index = i の値を求める
        """
        return self.query(i, i+1)


    def __str__(self):
        """元の配列を出力
        """
        for i in range(self.size):
            self.__getitem__(i)
        return " ".join(map(str, self.data[self.size:]))

####################################
class LazySegmentTree_RUQ:
    """RUQRangeQuery
    区間更新・区間Min/Sum
    Parameters
    ----------
    a : list
        初期リスト
    e : 単位元
        by default float('inf')
    Attributes
    ----------
    log : int
        木の高さ
    size : int
        木のノード数
    data : list
        木のノードの値
    lazy : list
        遅延評価用値
    """
    def __init__(self, a:list, f, ie, type) -> None:
        self.type = type.lower()
        self.f = f
        self.INF = ie
        self.log = len(a).bit_length()
        self.size = 1 << self.log
        self.data = [self.INF] * (2*self.size)
        self.lazy = [None] * (2*self.size)
        for i, ai in enumerate(a):
            self.data[i + self.size] = ai
        for i in range(self.size)[::-1]:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])

    def _prop_value(self, v):
        if self.type == 'min':
            return v
        elif self.type == 'sum':
            return v // 2

    def _update_value(self, x):
        if self.type == 'min':
            return x
        elif self.type == 'sum':
            return x * 2

    def __gindex(self, l, r):
        """伝搬される区間のインデックス(1-indexed)を全て列挙するgenerator
        """
        L = l + self.size; R = r + self.size
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1


    def __propagates(self, *ids):
        """遅延伝搬処理
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None: continue
            v = self._prop_value(v)
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.data[2*i] = v
            self.data[2*i+1] = v
            self.lazy[i] = None


    def update(self, l: int, r: int, x: int) -> None:
        """半開区間[l, r)に対して値をxに更新
        """
        *ids, = self.__gindex(l, r)
        self.__propagates(*ids)
        L = self.size + l; R = self.size + r
        xx = x
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R] = xx
                self.data[R] = xx
            if L & 1:
                self.lazy[L] = xx
                self.data[L] = xx
                L += 1
            L >>= 1; R >>= 1
            xx = self._update_value(xx)
        for i in ids:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])


    def query(self, l: int, r: int) -> None:
        """半開区間[l, r)内のfを求める
        """
        self.__propagates(*self.__gindex(l, r))
        L = self.size + l; R = self.size + r

        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = self.f(s, self.data[R])
            if L & 1:
                s = self.f(s, self.data[L])
                L += 1
            L >>= 1; R >>= 1
        return s


    def __getitem__(self, i:int) -> int:
        """index = i の値を求める
        """
        return self.query(i, i+1)


    def __str__(self):
        """元の配列を出力
        """
        for i in range(self.size):
            self.__getitem__(i)
        return " ".join(map(str, self.data[self.size:]))


####################################
# Range Minimum Query
class RAQRMQ(LazySegmentTree_RAQ):
    def __init__(self, a):
        super().__init__(a, min, float('inf') ,'min')

# Range Sum Query
class RAQRSQ(LazySegmentTree_RAQ):
    def __init__(self, a):
        super().__init__(a, lambda x, y: x+y, 0 ,'sum')

####################################
# Range Minimum Query
class RUQRMQ(LazySegmentTree_RUQ):
    def __init__(self, a):
        super().__init__(a, min, 2**31-1 ,'min')

# Range Sum Query
class RUQRSQ(LazySegmentTree_RUQ):
    def __init__(self, a):
        super().__init__(a, lambda x, y: x+y, 0 ,'sum')

####################################

n, q = map(int, input().split())
lst = RAQRSQ([0]*n)
lst = RAQRMQ([0]*n)
lst = RUQRMQ([2**31-1] * n)
lst = RUQRSQ([0]*n)

ret = []
for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, x = qry
        r += 1
        lst.update(l, r, x)
    else:
        l, r = qry
        r += 1
        ret.append(lst.query(l, r))
print('\n'.join(map(str, ret)))

#prefix#
# Lib_Q_LazySeg_区間Add,Update x 区間Min,Sumクエリ
#end#

