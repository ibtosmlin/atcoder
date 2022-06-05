n = int(input())

prod = [1]
for i in range(1, n):
    prod.append(prod[-1] * i)

def ncr(n, r):
    if r == 0 or r == n:
        return 1
    return prod[n] // prod[r] // prod[n-r]

for k in range(n):
    print(*[ncr(k, l) for l in range(k+1)])
