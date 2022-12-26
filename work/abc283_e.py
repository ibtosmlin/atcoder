# https://atcoder.jp/contests/abc283/tasks/abc283_e
INF = 10**9
def end(r=-1): print(r); exit()
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)

n, m = map(int, input().split())
A = []
for _ in range(n):
    a = tuple(map(int, input().split()))
    b = tuple(1-ai for ai in a)
    A.append((a, b))


def isalone(j, B):
    # (1, j)
    i = 1
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if isinhw(ni, nj, 3, m):
            if B[ni][nj] == B[i][j]:
                return False
    return True

def checkrow(u, v, w):
    # returns when determine a[i] , a[i-1] is ok or ng
    for j in range(m):
        if isalone(j, [u, v, w]):
            return False
    return True

if n == 2:
    ret = INF
    if checkrow(A[0][0], A[1][0], A[1][1]) and checkrow(A[0][1], A[0][0], A[1][0]):
        ret = min(ret, 0)
    if checkrow(A[0][0], A[1][1], A[1][0]) and checkrow(A[0][1], A[0][0], A[1][1]):
        ret = min(ret, 1)
    print(-1 if ret == INF else ret)
    exit()

dp = [[INF] * 2 for _ in range(2)]
if checkrow(A[0][1], A[0][0], A[1][0]): dp[0][0] = 0
if checkrow(A[0][0], A[0][1], A[1][0]): dp[1][0] = 1
if checkrow(A[0][1], A[0][0], A[1][1]): dp[0][1] = 1
if checkrow(A[0][0], A[0][1], A[1][1]): dp[0][0] = 0
#print(dp)
for i in range(1, n-1):
    ndp = [[INF] * 2 for _ in range(2)]
    au = A[i-1]
    av = A[i]
    aw = A[i+1]
    for u in range(2):
        for v in range(2):
            if dp[u][v] == INF: continue
            for w in range(2):
                if checkrow(au[u], av[v], aw[w]):
                    ndp[v][w] = min(ndp[v][w], dp[u][v] + w)
    dp = ndp
#    print(dp)
ret = INF
if checkrow(A[n-2][0], A[n-1][0], A[n-1][1]): ret = min(ret, dp[0][0])
if checkrow(A[n-2][0], A[n-1][1], A[n-1][0]): ret = min(ret, dp[0][1])
if checkrow(A[n-2][1], A[n-1][0], A[n-1][1]): ret = min(ret, dp[1][0])
if checkrow(A[n-2][1], A[n-1][1], A[n-1][0]): ret = min(ret, dp[1][1])
print(-1 if ret == INF else ret)
