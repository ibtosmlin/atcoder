a, b, x = map(int, input().split())

# a * n + b * d(n)
# Σ a * (10 ** i) * ui  + b * ui
# Σ (a * (10 ** i) + b) * ui

p = []
ten = 1
for i in range(20):
    p.append(ten * a + b)
    ten *= 10

p = reversed(p)

ret = []
for pi in p:
    u = x // pi
    ret.append(u)
    x -= u * pi
ret = int(''.join(map(str, ret)))
ret = min(10**9, ret)
print(ret)
