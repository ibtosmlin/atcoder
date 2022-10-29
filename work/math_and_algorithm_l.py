n = int(input())
for p in range(2, int(n**0.5)+1):
    if n%p==0:
        print('No')
        exit()
print('Yes')
