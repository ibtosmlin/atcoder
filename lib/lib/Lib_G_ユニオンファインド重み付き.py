#title#
# ユニオンファインド重み付き（ポテンシャル）

#subtitle#
# UnionFindWeighted(n)
# .find(x): xの親
# .unite(x, y, w): x　と　y　の差を　w として結合
# .weight(x):　xの重み
# .diff(x, y):　x と　y　の重みの差

#name#
# ユニオンファインド重み付き
#description#
# ユニオンファインド重み付き
#body#
class UnionFindWeighted:
    def __init__(self, n):                      # 初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.weights = [0] * n                  # 親との重み
        self.isvalid = [True] * n               # ポテンシャルがプラスの閉路あり

    #親を出力
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            p = self.find(self.parents[x])
            self.weights[x] += self.weights[self.parents[x]]
            self.parents[x] = p
            return p

    # ユニオン
    def unite(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            if self.diff(x, y) != w:
                self.isvalid[rx] = False
                return "invalid"
            else:
                return "pass"
        # a[x]->a[y]  の差はw  # a[y] = a[x] + w
        wx = self.weight(x)
        wy = self.weight(y)
        if rx == ry: return
        if self.ranks[rx] > self.ranks[ry]:
            rx , ry = ry, rx    #ryを親にする
            wx , wy = wy, wx
            w *= -1
        self.parents[rx] = ry
        self.sizes[ry] += self.sizes[rx]
        self.weights[rx] = wy - wx - w
        if self.ranks[rx]==self.ranks[ry]:
            self.ranks[rx] += 1
        self.isvalid[ry] &= self.isvalid[rx]
        return "unite"

    #xとyが同じグループかどうか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #xと同じグループの要素
    def members(self, x):
        root = self.find(x)
        return {i for i in range(self.n) if self.find(i) == root}

    #グループの要素数
    def size(self, x):
        root = self.find(x)
        return self.sizes[root]

    #親の要素一覧
    def roots(self):
        return {i for i, x in enumerate(self.parents) if i == x}

    #グループの個数
    def group_count(self):
        return len(self.roots())

    #グループのメンバー一覧
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    #重みの差
    def weight(self, x):
        _ = self.find(x)
        return self.weights[x]

    #重み
    def diff(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry: return float('inf')
        return self.weight(y) - self.weight(x)

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

################

n, m = map(int, input().split())
uf = UnionFindWeighted(n)
for _ in range(m):
    a, b, w = map(int,input().split())
    a -= 1; b -= 1
    uf.unite(a, b, w)

#prefix#
# Lib_G_unionfind_weighted
#end#
