n = int(input())
a = [input() for _ in range(n)]
ret = a[0]+a[1]
for i in range(n):
    for j in range(i+1, n):
        ret = min(ret, a[i]+a[j], a[j]+a[i])
print(ret)