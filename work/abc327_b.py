B = int(input())
a = 1; p = 1
while p < B:
    a += 1; p = pow(a, a)
print(a if p == B else -1)
