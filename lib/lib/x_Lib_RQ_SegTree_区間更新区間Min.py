#name#
# 遅延評価セグメント木区間更新区間Min
#description#
# 遅延評価セグメント木区間更新区間Min
#body#
import sys
def input(): return sys.stdin.readline().rstrip()

class LazySegmentTree:  # 初期化処理
    """RMQRUQ
    区間更新・区間Min
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
        self.log = (len(a)-1).bit_length()
        self.size = 1 << self.log
        self.data = [self.INF] * (2*self.size)
        self.lazy = [None] * (2*self.size)
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
            if v is None:
                continue
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v  # Update
            self.data[2*i] = v
            self.data[2*i+1] = v  # Update
            self.lazy[i] = None


    def update(self, l: int, r: int, x: int) -> None:
        """半開区間[l, r)に対して値をxに更新
        """
        *ids, = self.__gindex(l, r)
        self.__propagates(*ids)
        L = self.size + l; R = self.size + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R] = x
                self.data[R] = x    # Update
            if L & 1:
                self.lazy[L] = x
                self.data[L] = x    # Update
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])  # query


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
# Range Minimum Query
def op(x, y):
    return min(x, y)
ie = float('inf')

n, q = map(int, input().split())
ie = 2**31-1
a = [ie] * n
ruq = LazySegmentTree(a, op, ie)

ret = []
for _ in range(q):
    t, *qry = map(int, input().split())
    if t == 0:
        l, r, x = qry
        r += 1
        ruq.update(l, r, x)
    else:
        l, r = qry
        r += 1
        ret.append(ruq.query(l, r))
print('\n'.join(map(str, ret)))

#prefix#
# Lib_Seg_区間更新区間Min
#end#
