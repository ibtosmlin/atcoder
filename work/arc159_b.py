# https://atcoder.jp/contests/arc159/tasks/arc159_b
from math import gcd

INF = 10**18
A, B = map(int, input().split())
if A == B: print(1); exit()

if A > B: A, B = B, A
D = B - A
PS = []
for i in range(2, int(D**0.5)+1):
    if D%i == 0:
        while D%i == 0:
            D //= i
        PS.append(i)
if D > 1:
    PS.append(D)
ret = 0
while A > 0 and B > 0:
    g = gcd(A, B)
    A //= g; B //= g
    x = A
    for p in PS:
        if (B - A) % p == 0:
            x = min(x, A%p)
    ret += x
    A -= x
    B -= x

print(ret)
