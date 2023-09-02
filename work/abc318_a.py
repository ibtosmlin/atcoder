# https://atcoder.jp/contests/abc318/tasks/abc318_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

n, m, p = map(int, input().split())
print(len(list(range(m, n+1, p))))
