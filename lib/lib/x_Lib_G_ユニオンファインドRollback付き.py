#title#
# ユニオンファインドRollback付き
#subtitle#
# UnionFindRollback(n)
# .find(x): xの親
# .unite(x, y, w): x と y の差を w として結合
# もし、不整合だったら"invalid"を返す
# .is_same(x, y): 同じグループかどうか

#name#
# ユニオンファインド
#description#
# ユニオンファインド
#body#

class UnionFindRollback:
    def __init__(self, n):                      # 初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.leaders = None                     # リーダー
        self.groups = None                      # グループ
        self.history = []                       # 履歴

    def find(self, x):
        if self.parents[x] == x: return x
        self.parents[x] = p = self.find(self.parents[x])
        return p

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.history.append((x, -1, -1, -1))
            return
        if self.ranks[x] > self.ranks[y]:
            x , y = y, x    #yを親にする
        elif self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        self.parents[x] = y
        self.sizes[y] += self.sizes[x]
        self.history.append((x, y, , -1))

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x):
        """xのグループの要素数"""
        return self.sizes[self.find(x)]

    def get_groups(self):
        """親のリスト取得
            親ごとのグループのメンバー一覧取得
        """
        leader_buf = [self.find(i) for i in range(self.n)]
        self.leaders = []
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            if leader_buf[i] == i:
                self.leaders.append(i)
            result[leader_buf[i]].append(i)
        self.gropus = result
        return result

    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.leaders)

################

n, q = map(int, input().split())
uf = UnionFind(n)
for _ in range(q):
    p, a, b = map(int,input().split())
    a -= 1; b -= 1
    if p == 0:
        uf.unite(a, b)
    else:
        if uf.is_same(a, b):
            print('Yes')
        else:
            print('No')

# https://atcoder.jp/contests/atc001/tasks/unionfind_a

#prefix#
# Lib_G_unionfind
#end#
