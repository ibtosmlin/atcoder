# https://atcoder.jp/contests/abc319/tasks/abc319_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

INF = 10**10
n, m = map(int, input().split())
G = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int1, input().split())
    G[a].add(b)
    G[b].add(a)


dp = [0] * n
depth = [INF] * n
dp[0] = 0
depth[0] = 0

