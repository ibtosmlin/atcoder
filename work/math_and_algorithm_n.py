n = int(input())
ret = []
for p in range(2, int(n**0.5)+1):
    while n%p == 0:
        n //= p
        ret.append(p)
if n != 1:
    ret.append(n)
print(*ret)