n = int(input())
a = list(map(int, input().split()))
ret = set()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            ret.add(a[i]*a[j]*a[k])
print(len(ret))