# https://atcoder.jp/contests/abc319/tasks/abc319_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())

G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)


# dp[S]:= これまでに飲んだ薬の集合が
# S であるときの高橋くんの強さとしてありえる最大値