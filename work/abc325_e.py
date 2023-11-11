# https://atcoder.jp/contests/abc325/tasks/abc325_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1


from heapq import heappop, heappush
def dijkstra(n, G, start):
    INF = 10 ** 20
    dist = [INF] * n
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, x = heappop(que)
        if d != dist[x]: continue
        for nx in range(n):
            if x == nx: continue
            nd = d + G[x][nx]
            if nd >= dist[nx]: continue
            dist[nx] = nd
            heappush(que, (nd, nx))
    return dist



N, A, B, C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(N)]

G0 = [[0] * N for _ in range(N)]
G1 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        G0[i][j] = D[i][j] * A
        G1[i][j] = D[i][j] * B + C

F = dijkstra(N, G0, 0)
R = dijkstra(N, G1, N-1)

ret = 10**20
for f, r in zip(F, R):
    ret = min(ret, f+r)
print(ret)