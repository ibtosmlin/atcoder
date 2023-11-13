
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
from itertools import *

N, M, K = map(int, input().split())
C = list(combinations(range(M), N-1))   # 組み合わせ(nCr)
E = []
for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    E.append((a, b, w))
E.sort(key=lambda x: x[2])

def f(c):
    uf = UnionFind(N)
    ret = 0
    for ci in c:
        a, b, w = E[ci]
        if uf.same(a, b): return K * 2
        uf.unite(a, b)
        ret += w
        ret %= K
    return ret

ret = K
for c in C:
    ret = min(ret, f(c))
print(ret)



# https://atcoder.jp/contests/atc001/tasks/unionfind_a
