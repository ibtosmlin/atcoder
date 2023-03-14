def f(a, x, m):
    if x == 1:
        return 1%m
    if x%2:
        return (1 + a*f(a, x-1, m)) % m
    return f(a, x//2, m) * (1+pow(a, x//2, m)) % m

a, x, m = map(int, input().split())
print(f(a,x,m))
