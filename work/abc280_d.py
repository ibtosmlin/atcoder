# https://atcoder.jp/contests/abc280/tasks/abc280_d
##############################
# 素因数分解
# nは10**15くらいまでOK
# returns dict s.t. key = {prime}   value = {degree}
##############################
def prime_factorize(n:int) -> dict:
    if n == 1: return {1: 1}
    pd = dict()
    for p in range(2, int(n**0.5)+1):
        if n % p != 0: continue
        d = 0
        while n % p == 0:
            d += 1
            n //= p
        pd[p] = d
    if n != 1: pd[n] = 1
    return pd

##############################
# n!が素数pで何回割れるか O(logn)
# legendre(n, p)
##############################
def legendre(n, p):
    ret = 0
    while n > 0:
        ret += n // p
        n //= p
    return ret

k = int(input())
x = prime_factorize(k)

def isok(m):
    for p, v in x.items():
        if legendre(m, p) < v:
            return False
    return True

ok = k
ng = 1
while ok-ng > 1:
    mid = (ok+ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
