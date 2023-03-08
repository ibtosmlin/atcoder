from collections import defaultdict
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
        return {i for i in range(self.n) if self.find(i) == root}

    def size(self, x):
        """xのグループの要素数
        """
        return self.sizes[self.find(x)]

    @property
    def roots(self):
        """親の要素一覧
        """
        return {i for i, x in enumerate(self.parents) if i == x}

    @property
    def all_group_members(self):
        """グループのメンバー一覧
        """
        group_members = defaultdict(list)
        for x in range(self.n):
            group_members[self.find(x)].append(x)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.roots)

################

n, m = map(int, input().split())
uf = UnionFind(n)
G = [0] * n
for _ in range(m):
    _a, _b = map(int,input().split())
    _a -= 1; _b -= 1
    uf.unite(_a, _b)
    G[_a] += 1
    G[_b] += 1

for v in uf.all_group_members.values():
    node = 0
    edge = 0
    for u in v:
        node += 1
        edge += G[u]
    if node != edge//2:
        print('No')
        break
else:
    print('Yes')

