n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)
q = int(input())
Queries = []
for _ in range(q):
    v, d, c = map(int, input().split())
    v -= 1
    Queries.append((v, d, c))
Queries = Queries[::-1]

color = [0] * n
seen = [False] * 1001001
def func(d, v, c):
    if seen[v * 11 + d]: return
    for i in range(d+1):
        seen[v * 11 + i] = True
    if color[v] == 0:
        color[v] = c
    if d > 0:
        for w in G[v]:
            if seen[w * 11 + d -1]: continue
            func(d-1, w, c)
    return

for v, d, c in Queries:
    func(d, v, c)
print('\n'.join(map(str, color)))
