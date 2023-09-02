# https://atcoder.jp/contests/abc318/tasks/abc318_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

g = set()
n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]

for a, b, c, d in s:
    for i in range(a, b):
        for j in range(c, d):
            g.add(i*101+j)
print(len(g))
