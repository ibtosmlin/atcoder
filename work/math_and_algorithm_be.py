# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_be
import math
n, k = map(int, input().split())
v = list(map(int, input().split()))

ret = 0
for i in range(1, 1<<k):
    bitcount = 0
    vs = []
    for j in range(k):
        if i >> j & 1:
            bitcount +=1
            vs.append(v[j])
    mcd = vs[0]
    for vsi in vs[1:]:
        gcd = math.gcd(mcd, vsi)
        mcd *= vsi
        mcd //= gcd
    if bitcount%2:
        ret += n//mcd
    else:
        ret -= n//mcd
print(ret)