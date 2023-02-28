# python3
# https://atcoder.jp/contests/abc291/tasks/abc291_f
n, m = map(int, input().split())
GFor = [[] for _ in range(n)]
GBack = [[] for _ in range(n)]
Skip_edges = [[] for _ in range(n)]
for fm in range(n):
    s = input()
    for j, sj in enumerate(s):
        if int(sj):
            to = fm + j + 1
            GFor[fm].append(to)
            GBack[to].append(fm)
            for u in range(fm+1, to):
                Skip_edges[u].append((fm, to))

INF = 10**9
dpF = [INF] * n
dpF[0] = 0
for x in range(n):
    for nx in GFor[x]:
        dpF[nx] = min(dpF[nx], dpF[x] + 1)

dpB = [INF] * n
dpB[-1] = 0
for x in range(n)[::-1]:
    for nx in GBack[x]:
        dpB[nx] = min(dpB[nx], dpB[x] + 1)

ret = []
for i in range(1, n-1):
    nw = INF
    for u, v in Skip_edges[i]:
        nw = min(nw, dpF[u] + dpB[v] + 1)
    if nw == INF: nw = -1
    ret.append(nw)
print(*ret)
