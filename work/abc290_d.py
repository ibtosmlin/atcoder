from math import gcd

def solv(N, D, K):
    g = gcd(N, D)
    n = N // g
    d = D // g
    K -= 1
    return K // n + (K * D % N)



t = int(input())
for _ in range(t):
    n, d, k = map(int, input().split())
    print(solv(n, d, k))
