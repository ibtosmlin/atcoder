n=int(input())
ret = 0
for i in range(1, 1<<n):
    u = bin(i).count('1')
    ret += 9 ** (n-u)
print(ret)