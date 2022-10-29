INF = 1<<30
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
a = list(zip(*a))

memop = dict()
def p(x, u):
    if (x, u) in memop:
        return memop[(x, u)]
    ret = 0
    for i in range(m):
        if u >> i & 1 == 0:
            ret += a[x][i]
    memop[(x, u)] = ret
    return ret

def cnt(i, j, uvw):
    ret = 0
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if 0<= ni < 3 and 0<= nj < m:
            if uvw[ni] >> nj & 1:
                ret += 1
    return ret

memoisok = dict()
def isok(u, v, w):
    if (u, v, w) in memoisok:
        return memoisok[(u, v, w)]
    uvw = [u, v, w]
    for i in range(3):
        for j in range(m):
            if uvw[i] >> j & 1 == 0: continue
            if cnt(i, j, uvw) > 2:
                memoisok[(u, v, w)] = False
                return False
    memoisok[(u, v, w)] = True
    return True


dp = [[INF] * (1<<m) for __ in range(1<<m)]
dp[0][0] = 0

for i in range(n):
    ndp = [[INF] * (1<<m) for __ in range(1<<m)]
    for u in range(1<<m):
        for v in range(1<<m):
            prev = dp[u][v]
            if prev == INF: continue
            for w in range(1<<m):
                if not isok(u, v, w): continue
                ndp[v][w] = min(ndp[v][w], prev + p(i, w))
    dp = ndp

ret = INF
for u in range(1<<m):
    for v in range(1<<m):
        ret = min(ret, dp[u][v])
print(ret)
