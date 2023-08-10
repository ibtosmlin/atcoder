from math import gcd
N, M = map(int, input().split())
g = gcd(N, M)

N //= g
M //= g

r = N%M
ret = g* ((M - r)%M)
print(ret)