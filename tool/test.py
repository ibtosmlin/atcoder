######################################
INF = 10 ** 9
n, m = map(int, input().split())
G = []
d = [INF for _ in range(n)]
d[0] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    d[v] = min(d[v], d[u] + w)

print(*d)