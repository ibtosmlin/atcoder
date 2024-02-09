# https://atcoder.jp/contests/practice2/tasks/practice2_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

from atcoder.fenwicktree import FenwickTree as FT

class FenwickTree(FT):
    def __init__(self, A):
        if type(A) == int:
            super().__init__(A)
        else:
            super().__init__(len(A))
            for i, ai in enumerate(A):
                self.add(i, ai)

    def __getitem__(self, i):
        return self.sum(i, i+1)

    def __str__(self):
        s = "V: "
        s += " ".join(map(str, [self[i] for i in range(self._n)]))
        s += "\nR: "
        s += " ".join(map(str, [self._sum(i) for i in range(self._n+1)]))
        return s

    def update(self, p: int, x) -> None:
        assert 0 <= p < self._n
        self.add(p, x - self[p])

    def bisect_right(self, x):
        # pos: sum([0, pos)) > x     となる最大のindex
        _sum, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self._n and _sum + self.dat[k] <= x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def bisect_left(self, x):
        # pos: sum([0, pos)) > x     となる最大のindex
        _sum, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self._n and _sum + self.dat[k] <= x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos


n, q = map(int, input().split())
A = list(map(int, input().split()))
ft = FenwickTree(A)
ret = []
for _ in range(q):
    f, x, y = map(int, input().split())
    if f == 0:
        ft.add(x, y)
    else:
        ret.append(ft.sum(x, y))
print('\n'.join(map(str, ret)))
print(ft)
ft.update(u)