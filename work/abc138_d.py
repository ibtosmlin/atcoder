# https://atcoder.jp/contests/abc138/tasks/abc138_d
import sys
sys.setrecursionlimit(10**9)

n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

counter = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    counter[p] += x

def dfs(x=0, p=-1):
    global counter
    for nx in G[x]:
        if nx == p: continue
        counter[nx] += counter[x]
        dfs(nx, x)
    return

dfs()

print(*counter)