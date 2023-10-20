# https://atcoder.jp/contests/abc238/tasks/abc238_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, q = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    G[a].append(b)
    G[b].append(a)

seen  = [False] * (n+1)
def dfs(x, p=-1):
    seen[x] = True
    for nx in G[x]:
        if nx == p: continue
        if seen[nx]: continue
        if nx == n:
            exit(print('Yes'))
        dfs(nx, x)

dfs(0)
print('No')