#name#
# 遅延評価セグメント木
#description#
# 遅延評価セグメント木
#body# takayag
import sys
def input(): return sys.stdin.readline().rstrip()

class LazySegmentTree:  # 初期化処理
    """RSQRAQ
    区間加算・区間Sum
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
    def __init__(self, a:list, f, ie) -> None:
        self.f = f
        self.INF = ie
        self.n = len(a)
        self.log = (len(a)-1).bit_length()
        self.size = 1 << self.log
        self.data = [self.INF] * (2*self.size)
        self.lazy = [0] * (2*self.size)
        for i, ai in enumerate(a):
            self.data[i + self.size] = ai
        for i in range(self.size)[::-1]:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])


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
            if not v:
                continue
            self.lazy[2*i] += v//2
            self.lazy[2*i+1] += v//2
            self.data[2*i] += v//2
            self.data[2*i+1] += v//2
            self.lazy[i] = 0


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
                self.lazy[R] += xx
                self.data[R] += xx
            if L & 1:
                self.lazy[L] += xx
                self.data[L] += xx
                L += 1
            L >>= 1; R >>= 1
            xx *= 2
        for i in ids:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])  # query
            self.data[i] += self.lazy[i]  # query


    def query(self, l: int, r: int) -> None:
        """半開区間[l, r)内のfを求める
        """
        self.__propagates(*self.__gindex(l, r))
        L = self.size + l; R = self.size + r

        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = self.f(s, self.data[R])  # query
            if L & 1:
                s = self.f(s, self.data[L])  # query
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
# Range Sum Query
def op(x, y):
    return x + y
ie = 0

n, q = map(int, input().split())
ie = 0
a = [ie] * n
ruq = LazySegmentTree(a, op, ie)
ret = []
for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, x = qry
        l -= 1
#        r += 1
        ruq.update(l, r, x)
    else:
        l, r = qry
        l -= 1
#        r += 1
        ret.append(ruq.query(l, r))
print('\n'.join(map(str, ret)))


#prefix#
# Lib_Q_seg木（区間加算・区間Sum)
#end#
