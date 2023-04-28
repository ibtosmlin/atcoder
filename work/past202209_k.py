import sys
sys.setrecursionlimit(10**8)

class UnionFind:
    def __init__(self, n):                      # 初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.group_count = n                    # グループの数


    def find(self, x):
        """親を出力
        Parameters
        ----------
        x : int
            ノード番号
        """
        if self.parents[x] == x: return x
        self.parents[x] = p = self.find(self.parents[x])
        return p

    def unite(self, x, y):
        """ユニオン
        """
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]:
            x , y = y, x    #yを親にする
        elif self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        self.parents[x] = y
        self.sizes[y] += self.sizes[x]
        self.group_count -= 1

    def same(self, x, y) -> bool:
        """xとyが同じグループかどうか
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """xと同じグループの要素
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def size(self, x):
        """xのグループの要素数
        """
        return self.sizes[self.find(x)]

    def get_roots(self):
        """親のリスト取得
           親ごとのグループのメンバー一覧取得
        """
        _dum = [[] for _ in range(self.n)]
        self.roots = []
        self.group_members = dict()
        for x in range(self.n):
            r = self.find(x)
            if r == x:
                self.roots.append(r)
            _dum[r].append(x)
        for r in self.roots:
            self.group_members[r] = _dum[r]


    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.roots)

################

# https://atcoder.jp/contests/atc001/tasks/unionfind_a


n, m = map(int, input().split())
E = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    E[a].append(b)

q = int(input())
Q = []
for _ in range(q):
    t, x, y = map(int, input().split())
    Q.append((t, x-1, y-1))
for t, x, y in Q:
    if t == 1:
        E[x].append(y)
    elif t == 2:
        E[x].remove(y)

ret = []
uf = UnionFind(n)
for x in range(n):
    for y in E[x]:
        uf.unite(x, y)

for t, x, y in reversed(Q):
    if t == 2:
        E[x].append(y)
        uf.unite(x, y)
    elif t == 1:
        E[x].remove(y)
        uf = UnionFind(n)
        for x in range(n):
            for y in E[x]:
                uf.unite(x, y)
    else:
        ret.append(uf.same(x, y))

for ri in reversed(ret):
    print('Yes' if ri else 'No')
