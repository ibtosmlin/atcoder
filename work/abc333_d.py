# https://atcoder.jp/contests/abc333/tasks/abc333_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

##########################################
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

if len(G[0]) == 1:
    exit(print(1))

child = [0] * n
def dfs(x, p=-1):
    global child
    ret = 1
    for nx in G[x]:
        if p == nx: continue
        ret += dfs(nx, x)
    child[x] = ret
    return ret
dfs(0)


ret = [child[x] for x in G[0]]
ret = sum(ret) - max(ret)
print(ret+1)
