# https://atcoder.jp/contests/joig2022-open/tasks/joig2022_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

from collections import defaultdict

isinhw = lambda i,j,h,w: (0 <= i < h) and (0 <= j < w)
notinhw = lambda i,j,h,w: not ((0 <= i < h) and (0 <= j < w))


h, w = map(int, input().split())
D = defaultdict(int)
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    for da in range(-1, 2):
        for db in range(-1, 2):
            u = (a + da) * w + (b+db)
            D[u] += 1
print(max(D.values()))