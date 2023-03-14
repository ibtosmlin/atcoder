# https://atcoder.jp/contests/abc293/tasks/abc293_f

def B(d, n):
    l = 1
    r = n+1
    while r-l>1:
        mid = (r+l) // 2
        pd = 1
        for i in range(d-1):
            pd *= mid
            if pd > n+1:
                pd = n+1
                break
        if pd <= n:
            l = mid
        else:
            r = mid
    return l


def iszo(b, n):
    now = n
    while now:
        if now%b > 1:
            return False
        now //= b
    return True

def solve(n):
    ret = set([n, n-1])
    d = 3
    now = n
    while 4 <= now:
        b = B(d, n)
        if iszo(b, n):
            ret.add(b)
        d += 1
        now //= 2
    return ret

t = int(input())
for _ in range(t):
    n = int(input())
    ret = solve(n)
    print(len(ret-set({1})))