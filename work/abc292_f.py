import cmath
a, b = map(int, input().split())
if a > b: a, b = b, a
r60 = cmath.rect(1, cmath.pi/3)

def isok(x):
    z = r60 * complex(a, x)
    u, v = z.real, z.imag
    return 0<= u <= a and 0 <= v <= b

ok = 0
ng = b
while ng-ok > 0.0000000001:
    mid = (ng+ok) / 2
    if isok(mid):
        ok = mid
    else:
        ng = mid

print((ok**2 + a**2) ** 0.5)
