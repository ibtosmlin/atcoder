mod = 10**9+7
a, b = map(int, input().split())
ret = 1
while b:
    if b%2: ret = a*ret%mod
    a = a*a%mod
    b //= 2

print(ret)