def end(x): print(x); exit()

n, m, k = map(int, input().split())
s = [1 if si == 'x' else 0 for si in input()]
t = [0]
for si in s:
    t.append(t[-1] + si)

def isok(l, r):
    ret = 0
    if r <= n:
        ret = t[r] - t[l]
    else:
        d = r - n
        lp = d // n
        ret = t[n] - t[l] + t[-1] * lp + t[d%n]
    return ret <= k


def solv(l):
    ok = l
    ng = n * m + 1
    while ng - ok > 1:
        mid = (ng+ok) // 2
        if isok(l, mid):
            ok = mid
        else:
            ng = mid
    return ok - l

ret = 0
for l in range(n):
    ret = max(ret, solv(l))
print(ret)

