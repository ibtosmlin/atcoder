import sys
input = sys.stdin.readline
from collections import deque


class ReRooting:
    def __init__(self, n, G) -> None:
        self.N = n
        self.oG = G[:]
        self.G = [G[i][:] for i in range(n)]

    def _topological_sort(self, root):
        P = [-1] * self.N
        Q = deque([root])
        R = []
        while Q:
            i = deque.popleft(Q)
            R.append(i)
            for a in self.G[i]:
                if a != P[i]:
                    P[a] = i
                    self.G[a].remove(i)
                    deque.append(Q, a)
        SIZE = [1] * self.N
        for i in R[1:][::-1]:
            SIZE[P[i]] += SIZE[i]
        self.P = P
        self.R = R
        self.SIZE = SIZE

    def build(self, root=0):
        self._topological_sort(root)
        N, P, R, G = self.N, self.P, self.R, self.G
        SIZE = self.SIZE

        ##### Settings
        unit = 0
        merge = lambda a, b: a + b
        adj_bu = lambda a, i: a / len(self.oG[i]) + 1
        adj_td = lambda a, i, p: a / (N-SIZE[i]) + 1
        adj_fin = lambda a, i: a * max(1, len(self.oG[i])) /
        #####

        ME = [unit] * N
        XX = [0] * N
        TD = [unit] * N
        for i in R[1:][::-1]:
            XX[i] = adj_bu(ME[i], i)
            p = P[i]
            ME[p] = merge(ME[p], XX[i])
        XX[R[root]] = adj_fin(ME[R[root]], R[root])

        for i in R:
            ac = TD[i]
            for j in G[i]:
                TD[j] = ac
                ac = merge(ac, XX[j])
            ac = unit
            for j in G[i][::-1]:
                TD[j] = adj_td(merge(TD[j], ac), j, i)
                ac = merge(ac, XX[j])
                XX[j] = adj_fin(merge(ME[j], TD[j]), j)
        self.XX = XX

########################################################


n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    x, y = map(lambda u: int(u)-1, input().split())
    G[x].append(y)
    G[y].append(x)

rr = ReRooting(n, G)
rr.build()


print('\n'.join(map(str, rr.XX)))
