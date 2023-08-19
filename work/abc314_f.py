# https://atcoder.jp/contests/abc314/tasks/abc314_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

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

n = int(input())
uf = UnionFind(n)
m = n - 1
N = n+m
G = [[] for _ in range(N)]
groupid = [i for i in range(n)]

for i in range(m):
    p, q = map(lambda x: int(x)-1, input().split())
    p = uf.find(p); gp = groupid[p]
    q = uf.find(q); gq = groupid[q]
    uf.unite(p, q)
    pq = uf.find(p)
    groupid[pq] = n + i
    G[gp].append(n+i)
    G[gq].append(n+i)
    G[n+i].append(gp)
    G[n+i].append(gq)


cnt = [1] * n + [0] * m
ret = [0] * N
mod = 998244353


def dfs(x, p=-1):
    global cnt
    now = cnt[x]
    for nx in G[x]:
        if nx == p: continue
        dfs(nx, x)
        now += cnt[nx]
    cnt[x] = now

def dfs2(x, p=-1):
    for nx in G[x]:
        if nx == p: continue
        ret[nx] += ret[x] + cnt[nx] * prob[cnt[x]]
        ret[nx] %= mod
        dfs2(nx, x)

dfs(N-1)
prob = {0:1}
for ci in cnt:
    if ci in prob: continue
    prob[ci] = pow(ci, -1, mod)
dfs2(N-1)

print(*ret[:n])
