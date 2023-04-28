# https://atcoder.jp/contests/past202209-open/tasks/past202209_h
N, X = map(int, input().split())
dp = [None] * (X+1)
dp[X] = (0, 10**9)
# dp[i]: bronze  value: g, s
for _ in range(N):
    ndp = [None] * (X+1)
    _s, _b, _g = map(int, input().split())
    for b in range(X+1):
        if dp[b] == None: continue
        g, s = ndp[b] = dp[b]
        nb, ng, ns = b - _b, g + _g, s - _s
        if nb < 0: continue
        if ndp[nb] and (ng, ns, nb) > (*ndp[nb], nb):
            ndp[nb] = (ng, ns)
        elif not ndp[nb]:
            ndp[nb] = (ng, ns)
    dp = ndp

ret = (0, 0, 0)
for b in range(X+1):
    if dp[b] == None: continue
    g, s = dp[b]
    if ret < (g, s, b):
        ret = (g, s, b)
print(*ret)
