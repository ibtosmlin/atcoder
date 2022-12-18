n,m,a,b = map(int, input().split())
isa = [0] * (n+2)
for _ in range(m):
    l, r = map(int, input().split())
    isa[l] += 1
    isa[r+1] -= 1

ca = 0
for i in range(n+1):
    if isa[i] > 0:
        ca += 1
    isa[i+1] += isa[i]

print(ca*a+(n-ca)*b)