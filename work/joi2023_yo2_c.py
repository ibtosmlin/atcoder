# https://atcoder.jp/contests/joi2023yo2/tasks/joi2023_yo2_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1


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

    def get_groups(self):
        """親のリスト取得
            親ごとのグループのメンバー一覧取得
        """
        leader_buf = [self.find(i) for i in range(self.n)]
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        self.groups = result
        return result

    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.roots)

################


h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

uf = UnionFind(h*w)
vals = set()

for i in range(h):
    for j in range(w):
        # right
        if j + 1 < w and A[i][j] == A[i][j+1]:
            uf.unite(i*w+j, i*w+j+1)
        # down
        if i + 1 < h and A[i][j] == A[i+1][j]:
            uf.unite(i*w+j, i*w+w+j)
        vals.add(A[i][j])


vals = sorted(vals)
n = len(vals)
valsid = {v:i for i, v in enumerate(vals)}

count = [0] * n
maxs = [0] * n

for i in range(h*w):
    if uf.parents[i] == i:
        u, v = divmod(i, w)
        j = valsid[A[u][v]]
        ufs = uf.sizes[i]
        count[j] += ufs
        maxs[j] = max(maxs[j], ufs)

print(vals)
print(count)
print(maxs)