# https://atcoder.jp/contests/abc317/tasks/abc317_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
from collections import defaultdict, Counter, deque

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))


seen = [False] * n
def dfs(x, seen):
    seen[x] = True
    ret = 0
    for nx, c in G[x]:
        if seen[nx]: continue
        ret = max(ret, c + dfs(nx, seen))
    seen[x] = False
    return ret

ret = 0
for i in range(n):
    ret = max(ret, dfs(i, seen))

print(ret)