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
        self.leaders = []
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            if leader_buf[i] == i:
                self.leaders.append(i)
            result[leader_buf[i]].append(i)
        self.groups = result
        self.groupcount = len(self.leaders)
        return

    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.roots)

################
from collections import defaultdict
direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

uf = UnionFind(h*w)
for i in range(h):
    for j in range(w):
        for di, dj in direc:
            ni = i + di
            nj = j + dj
            if notinhw(ni, nj, h, w): continue
            if A[i][j] == A[ni][nj]:
                uf.unite(i*w+j, ni*w+nj)

uf.get_groups()
C = defaultdict(int)
for p in uf.leaders:
    C[p] = len(uf.groups[p])

G = defaultdict(set)
for i in range(h):
    for j in range(w):
        pij = uf.find(i * w + j)
        for di, dj in direc:
            ni = i + di
            nj = j + dj
            if notinhw(ni, nj, h, w): continue
            qij = uf.find(ni * w + nj)
            if pij != qij:
                G[pij].add(qij)

ret = 0
for p in uf.leaders:
    D = defaultdict(int)
    D[-1] = 0
    for q in G[p]:
        u, v = divmod(q, w)
        D[A[u][v]] += C[q]
    ret = max(ret, max(D.values()) + C[p])

print(ret)