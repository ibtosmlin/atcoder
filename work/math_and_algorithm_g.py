from math import gcd
n, x, y = map(int, input().split())
xy = x * y // gcd(x, y)
print(n // x + n // y - n // xy)