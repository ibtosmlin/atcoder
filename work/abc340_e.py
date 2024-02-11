# https://atcoder.jp/contests/abc340/tasks/abc340_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from atcoder.lazysegtree import LazySegTree
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
raq = LazySegTree(max, 0, lambda x, y: x+y, lambda x, y: x+y, 0, A)
for bi in B:
    x = raq.prod(bi, bi+1)
    raq.apply(bi, bi+1, -x)
    u, v = divmod(x, n)
    raq.apply(0, n, u)
    l = (bi + 1) % n
    r = l + v
    if r <= n:
        raq.apply(l, r, 1)
    else:
        raq.apply(l, n, 1)
        raq.apply(0, (l+v)%n, 1)

print(*[raq.prod(i, i+1) for i in range(n)])
