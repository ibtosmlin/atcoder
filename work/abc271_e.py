import sys
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
INF = float('inf')
n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    edges.append((a, b, c))
el = list(map(int1, input().split()))

dist = [INF] * n
dist[0] = 0
for eli in el:
    a, b, c = edges[eli]
    if dist[a] == INF: continue
    dist[b] = min(dist[a] + c, dist[b])

if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])
