import sys
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

seen = [False] * n
ret = []
def dfs(x, p=-1):
    global ret
    seen[x] = True
    if x == n-1:
        ret.append(x+1)
        return True
    for nx in G[x]:
        if seen[nx]: continue
        if dfs(nx, x):
            ret.append(x+1)
            return True
    return False
dfs(0)
print(' '.join(map(str, ret[::-1])))