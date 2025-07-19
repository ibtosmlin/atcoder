class UnionFind:
    """木の深さが小さい方を親にする"""
    def __init__(self, n):
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.groups = dict()                    # グループ key:parent, value:listofmember
        self.ire = 0

    def find(self, x):
        if self.parents[x] == x: return x
        self.parents[x] = p = self.find(self.parents[x])
        return p

    def _choose_parent(self, x, y):
        """木の深さが大きい方を親とする"""
        if self.ranks[x] > self.ranks[y]:
            x, y = y, x
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        return x, y

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        x, y = self._choose_parent(x, y)
        self.parents[x] = y
        self.sizes[y] += self.sizes[x]

    def is_same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x):
        """xのグループの要素数"""
        return self.sizes[self.find(x)]

    def get_groups(self):
        """親のリスト取得
            親ごとのグループのメンバー一覧取得
        """
        self.groups = dict()
        for i in range(self.n):
            p = self.find(i)
            if p not in self.groups:
                self.groups[p] = []
            self.groups[p].append(i)
        return

    def __str__(self):
        self.get_groups()
        print(f'group_count = {len(self.groups)}')
        return ' '.join([f'{p}:{v}' for p, v in sorted(self.groups.items())])

direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # RULD
def isin(i, j, H, W): return (0 <= i < H) and (0 <= j < W)

H, W, N = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]
P = dict()
for i in range(H):
    for j in range(W):
        if not S[i][j] in P:
            P[S[i][j]] = []
        P[S[i][j]].append(i*W+j)
uf = UnionFind(H*W)

ret = 10**9
for v in sorted(P.keys(), reverse=True):
    for ij in P[v]:
        i, j = divmod(ij, W)
        for di, dj in direc:
            ni = i + di
            nj = j + dj
            if not isin(ni, nj, H, W): continue
            if S[ni][nj] >= v and not uf.is_same(ij, ni*W+nj):
                uf.unite(ij, ni*W+nj)
    groups = sum([1 for i, p in enumerate(uf.parents) if i == p and S[i//W][i%W] >= v])
    if groups == N:
        ret = min(ret, v)

ans = -1
for u in list(sorted(P.keys())):
    if u < ret:
        ans = u
    if u == ret:
        break
print(min(ans, ret-1))