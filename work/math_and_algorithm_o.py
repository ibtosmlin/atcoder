def gcd(x,y):
    if y == 0:
        return x
    x, y = y, x%y
    return gcd(x, y)
a, b = map(int, input().split())
print(gcd(a, b))