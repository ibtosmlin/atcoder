# https://atcoder.jp/contests/typical90/tasks/typical90_bj
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import deque

n = int(input())
G = [[] for _ in range(n)]
seen = [0] * n
ret = []

que = deque()
for i in range(n):
    a, b = map(int1, input().split())
    G[a].append(i)
    G[b].append(i)
    if i == a or i == b:
        que.append(i)
        seen[i] = 1
        ret.append(i+1)

while que:
    x = que.popleft()
    for nx in G[x]:
        if seen[nx]: continue
        seen[nx] = 1
        que.append(nx)
        ret.append(nx+1)

if len(ret) != n:
    print(-1)
else:
    for i in ret[::-1]:
        print(i)