# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_k
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from collections import defaultdict
n = int(input())
pair = [list(map(int, input().split())) for _ in range(n)]
nums = set()
for a, b in pair:
    nums.add(a)
    nums.add(b)
nid = {v:i for i, v in enumerate(sorted(nums))}
for i in range(n):
    for j in range(2):
        pair[i][j] = nid[pair[i][j]]

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
N = len(nid)

G = [0] * N
uf = UnionFind(N)
for a, b in pair:
    G[a] += 1
    G[b] += 1
    uf.unite(a, b)

ret = 0
x = uf.get_groups()
for g in x:
    ne = 0
    nn = 0
    for u in g:
        ne += G[u]
        nn += 1
    ret += min(nn, ne//2)
print(ret)