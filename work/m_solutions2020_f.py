# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_f
from collections import defaultdict
import bisect

INF = 10**10
n = int(input())
Airplains = []
for _ in range(n):
    x, y, u = input().split()
    x = int(x)
    y = int(y)
    Airplains.append((x, y, u))


def check(X):
    ret = INF
    ret = min(ret, checkUD(X))
    ret = min(ret, checkUR(X))
    return ret


def checkUD(X):
    ret = INF
    AU = defaultdict(list)
    AD = defaultdict(list)
    for x, y, u in X:
        if u == 'U':
            AU[x].append(y)
        if u == 'D':
            AD[x].append(y)
    for x in AU:
        if not x in AD: continue
        ADX = AD[x]
        ADX.sort()
        ADX.append(INF)
        for xi in AU[x]:
            u = bisect.bisect_left(ADX, xi)
            if ADX[u] == INF: continue
            ret = min(ret, (ADX[u] - xi)*5) # /0.2
    return ret

def checkUR(X):
    ret = INF
    AU = defaultdict(list)
    AR = defaultdict(list)
    for x, y, u in X:
        if u == 'U':
            AU[y-x].append(y)
        if u == 'L':
            AR[y-x].append(y)

    for x in AU:
        if not x in AR: continue
        ARX = AR[x]
        ARX.sort()
        ARX.append(INF)
        for xi in AU[x]:
            u = bisect.bisect_left(ARX, xi)
            if ARX[u] == INF: continue
            ret = min(ret, (ARX[u] - xi)*10) # /0.1
    return ret

def Trans(X):
    ts = {'U': 'L', 'R': 'U', 'D': 'R', 'L': 'D'}
    return [(-b, a, ts[s]) for a, b, s in X]

ret = INF
ret = min(check(Airplains), ret)
Airplains = Trans(Airplains)
ret = min(check(Airplains), ret)
Airplains = Trans(Airplains)
ret = min(check(Airplains), ret)
Airplains = Trans(Airplains)
ret = min(check(Airplains), ret)

print('SAFE' if ret == INF else ret)
